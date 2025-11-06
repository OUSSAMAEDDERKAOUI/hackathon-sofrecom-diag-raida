import os
import sys
import json
import logging
import traceback
from typing import Dict, List, Optional, Any, Tuple
import warnings

# Disable analytics and telemetry
os.environ["STREAMLIT_SERVER_ENABLE_STATIC_FILE_HANDLING"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

# Suppress specific warnings
warnings.filterwarnings('ignore', message='.*The frame.append method is deprecated.*')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True  # Force configuration to override any existing handlers
)
logger = logging.getLogger(__name__)

# Import Streamlit after environment variables are set
import streamlit as st
import requests

# Configure Streamlit page
st.set_page_config(
    page_title="Diag-Raida",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize session state
def init_session_state():
    if not hasattr(st.session_state, 'initialized'):
        st.session_state.initialized = True
        st.session_state.test_started = False
        st.session_state.test_id = None
        st.session_state.questions = []
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.session_state.results = None
        logger.info("Session state initialized")

# Initialize the session state
init_session_state()

# API configuration
BASE_URL = "http://127.0.0.1:5000"  # Using 127.0.0.1 is more reliable than localhost

# Sample resources for different topics (to be replaced with actual API call)
RESOURCES = {
    "algebra": [
        {"title": "Khan Academy - Algebra Basics", "url": "https://www.khanacademy.org/math/algebra"},
        {"title": "Paul's Online Math Notes - Algebra", "url": "https://tutorial.math.lamar.edu/"}
    ],
    "geometry": [
        {"title": "Khan Academy - Geometry", "url": "https://www.khanacademy.org/math/geometry"},
        {"title": "Math is Fun - Geometry", "url": "https://www.mathsisfun.com/geometry/"}
    ],
    "calculus": [
        {"title": "Khan Academy - Calculus", "url": "https://www.khanacademy.org/math/calculus-1"},
        {"title": "Paul's Online Math Notes - Calculus", "url": "https://tutorial.math.lamar.edu/"}
    ]
}

def init_session_state():
    if 'test_started' not in st.session_state:
        st.session_state.test_started = False
    if 'test_id' not in st.session_state:
        st.session_state.test_id = None
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'results' not in st.session_state:
        st.session_state.results = None

def start_test(num_questions: int = 5):
    try:
        # First, verify the API is accessible
        health_url = f"{BASE_URL}/health"
        try:
            # Try with CORS headers first
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
            
            logger.info(f"Checking backend health at: {health_url}")
            
            health_check = requests.get(
                health_url,
                timeout=5,  # 5 seconds timeout
                headers=headers
            )
            
            logger.info(f"Health check response: {health_check.status_code}")
            logger.debug(f"Response headers: {dict(health_check.headers)}")
            
            if health_check.status_code != 200:
                error_msg = (
                    f"Le serveur n'est pas prêt.\n"
                    f"URL: {health_url}\n"
                    f"Code: {health_check.status_code}\n"
                    f"Réponse: {health_check.text}"
                )
                logger.error(error_msg)
                st.error(error_msg)
                st.stop()
                
        except requests.exceptions.RequestException as e:
            error_msg = (
                "Impossible de se connecter au serveur.\n"
                f"URL: {health_url}\n"
                f"Erreur: {str(e)}\n\n"
                "Veuillez vérifier que:\n"
                "1. Le serveur backend est en cours d'exécution\n"
                f"2. L'URL du serveur est correcte: {BASE_URL}\n"
                "3. Aucun pare-feu ne bloque la connexion"
            )
            logger.error(error_msg)
            st.error(error_msg)
            st.stop()

        # Then request the test
        test_url = f"{BASE_URL}/api/diagnostic/test"
        logger.info(f"Requesting test from: {test_url}")
        response = requests.get(
            test_url,
            params={"num_questions": num_questions},
            headers={"Accept": "application/json"},
            timeout=10  # 10 seconds timeout
        )
        
        # Debug: Print the response
        print("Test response status:", response.status_code)
        print("Test response content:", response.text)
        
        response.raise_for_status()
        data = response.json()
        
        # Debug: Print the received data
        print("Test data received:", json.dumps(data, indent=2))
        
        # Ensure we have the expected data structure
        if 'test_id' not in data or 'questions' not in data:
            st.error("Format de réponse inattendu du serveur.")
            st.json(data)  # Show the actual response for debugging
            st.stop()
        
        # Add example answers to questions if not present
        for q in data['questions']:
            if 'example' not in q:
                q['example'] = "Ex: Pour une équation comme '2x + 3 = 7', écrivez 'x = 2'"
        
        st.session_state.test_id = data['test_id']
        st.session_state.questions = data['questions']
        st.session_state.test_started = True
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.session_state.results = None
        
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors du démarrage du test: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            st.error(f"Réponse du serveur: {e.response.text}")
        st.stop()
    except json.JSONDecodeError as e:
        st.error(f"Erreur lors de l'analyse de la réponse du serveur: {str(e)}")
        if hasattr(e, 'doc'):
            st.error(f"Contenu de la réponse: {e.doc}")
        st.stop()

def submit_test():
    try:
        if not st.session_state.answers:
            st.warning("Veuillez répondre à au moins une question avant de soumettre.")
            return
            
        # Prepare responses in the format expected by the backend
        responses = []
        for q_id, answer in st.session_state.answers.items():
            responses.append({
                "question_id": q_id,
                "answer": answer,
                "time_taken": 30,  # Placeholder - implement timing if needed
                "confidence": 0.8  # Placeholder - implement confidence if needed
            })
            
        payload = {
            "student_id": "streamlit_user",  # You can replace this with actual user ID if available
            "test_id": st.session_state.test_id,
            "responses": responses
        }
        
        logger.info("Submitting test with payload: %s", json.dumps(payload, indent=2))
        
        # Make the API request
        submit_url = f"{BASE_URL}/api/diagnostic/submit"
        logger.info(f"Submitting test to: {submit_url}")
        response = requests.post(
            submit_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30  # 30 seconds timeout
        )
        
        logger.info("Received response with status code: %s", response.status_code)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        try:
            results = response.json()
            logger.info("Parsed response: %s", json.dumps(results, indent=2))
            
            # Validate the response structure
            if not isinstance(results, dict):
                raise ValueError("Invalid response format: expected a JSON object")
                
            # Ensure we have the required fields
            if 'feedback' not in results:
                results['feedback'] = []
                
            # Add default values for missing fields
            results.setdefault('analysis', {'strengths': [], 'weaknesses': []})
            results.setdefault('recommendations', [])
            
            # Store the results
            st.session_state.results = results
            st.session_state.submitted = True
            
            logger.info("Test submitted successfully")
            
        except json.JSONDecodeError as e:
            logger.error("Failed to parse JSON response: %s", str(e))
            logger.error("Response content: %s", response.text)
            st.error("Erreur: La réponse du serveur est invalide. Veuillez réessayer.")
            
    except requests.exceptions.RequestException as e:
        error_msg = f"Erreur de connexion au serveur: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_details = e.response.json().get('detail', e.response.text)
                error_msg = f"{error_msg}\nDétails: {error_details}"
            except:
                error_msg = f"{error_msg}\nRéponse brute: {e.response.text[:500]}"
        
        logger.error(error_msg)
        st.error(error_msg)
        
    except Exception as e:
        error_msg = f"Une erreur inattendue s'est produite: {str(e)}"
        logger.exception("Unexpected error in submit_test")
        st.error(error_msg)
    
    # Force a rerun to update the UI
    st.rerun()

# Initialize session state
init_session_state()

def show_error(message: str, details: str = None):
    """Display an error message with optional details."""
    st.error(f"## ❌ Erreur\n{message}")
    if details:
        with st.expander("Détails techniques"):
            st.code(details)
    
    if st.button("🔄 Réessayer", type="primary"):
        st.session_state.test_started = False
        st.rerun()

# Main app
def main():
    try:
        st.title("🎯 Diag-Raida")
        st.subheader("Diagnostiquer, Comprendre, Réapprendre")
        
        # Check if we're in a healthy state
        if not hasattr(st.session_state, 'test_started'):
            init_session_state()
        
        if not st.session_state.test_started:
            show_welcome()
        elif st.session_state.submitted:
            show_results()
        else:
            show_question()
            
    except Exception as e:
        logger.exception("An unexpected error occurred")
        show_error(
            "Une erreur inattendue s'est produite. Veuillez réessayer.",
            f"{type(e).__name__}: {str(e)}\n\nStack trace:\n{str(traceback.format_exc())}"
        )

def show_welcome():
    st.write("""
    Bienvenue sur Diag-Raida — un outil intelligent pour diagnostiquer vos compétences en mathématiques.
    
    Ce test vous aidera à identifier vos forces et vos points d'amélioration.
    """)
    
    num_questions = st.slider("Nombre de questions :", 1, 20, 5)
    
    if st.button("Commencer le test", type="primary"):
        with st.spinner("Préparation du test..."):
            start_test(num_questions)
        st.rerun()

def show_question():
    if not st.session_state.questions:
        st.error("Aucune question disponible. Veuillez réessayer.")
        if st.button("Retour à l'accueil"):
            st.session_state.test_started = False
            st.rerun()
        return
    
    question = st.session_state.questions[st.session_state.current_question]
    
    # Progress and question counter
    progress = (st.session_state.current_question + 1) / len(st.session_state.questions)
    st.progress(progress)
    st.caption(f"Question {st.session_state.current_question + 1} sur {len(st.session_state.questions)}")
    
    # Display question with proper formatting
    st.markdown(f"### {question['text']}")
    
    # Show example answer format if available
    if 'example' in question:
        with st.expander("📝 Exemple de format de réponse attendue"):
            st.code(question['example'], language='text')
    
    # Text area for answer
    answer = st.text_area(
        "Votre réponse :",
        key=f"q_{question['id']}",
        value=st.session_state.answers.get(question['id'], ''),
        height=150,
        placeholder="Entrez votre réponse ici..."
    )
    
    # Save answer
    if answer:
        st.session_state.answers[question['id']] = answer
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("← Précédent"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.session_state.answers.get(question['id']):
            if st.session_state.current_question < len(st.session_state.questions) - 1:
                if st.button("Suivant →"):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Soumettre le test", type="primary"):
                    with st.spinner("Analyse de vos réponses..."):
                        submit_test()
                    st.rerun()
    
    with col3:
        if st.button("Annuler le test", type="secondary"):
            st.session_state.test_started = False
            st.rerun()

def show_results():
    if not st.session_state.results:
        st.error("Aucun résultat disponible.")
        if st.button("Retour à l'accueil"):
            st.session_state.test_started = False
            st.rerun()
        return
    
    results = st.session_state.results
    
    st.balloons()
    st.success("## 🎯 Analyse de vos résultats")
    
    # Display overall assessment
    st.markdown("### 📊 Évaluation globale")
    
    # Calculate overall score
    total_questions = len(results.get('feedback', []))
    correct_answers = sum(1 for f in results.get('feedback', []) if f.get('is_correct', False))
    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    
    # Display score with emoji based on performance
    if score_percentage >= 80:
        score_emoji = "🌟 Excellent !"
    elif score_percentage >= 60:
        score_emoji = "👍 Bien joué !"
    else:
        score_emoji = "💪 Continuez à vous améliorer !"
    
    st.metric("Score final", f"{correct_answers}/{total_questions} ({score_percentage:.0f}%)", score_emoji)
    
    # Display AI-powered insights
    st.markdown("### 🔍 Analyse détaillée")
    
    # Show strengths and weaknesses
    if 'analysis' in results:
        st.markdown("#### Points forts")
        if results['analysis'].get('strengths'):
            for strength in results['analysis']['strengths']:
                st.success(f"✓ {strength}")
        else:
            st.info("Aucun point fort significatif identifié.")
        
        st.markdown("#### Points à améliorer")
        if results['analysis'].get('weaknesses'):
            for weakness in results['analysis']['weaknesses']:
                st.error(f"⚠️ {weakness}")
        else:
            st.info("Aucun point faible majeur identifié.")
    
    # Display detailed feedback for each question
    st.markdown("### 📝 Détail des réponses")
    for i, feedback in enumerate(results.get('feedback', [])):
        with st.expander(f"Question {i + 1}: {feedback.get('topic', 'Sans thème')} - {'✓' if feedback.get('is_correct') else '✗'}"):
            st.markdown(f"**Question:** {feedback.get('question_text', '')}")
            
            # Show student's answer with visual feedback
            st.markdown("#### Votre réponse")
            if feedback.get('is_correct', False):
                st.success(feedback.get('student_answer', 'Aucune réponse fournie'))
            else:
                st.error(feedback.get('student_answer', 'Aucune réponse fournie'))
            
            # Show correct answer if wrong
            if not feedback.get('is_correct', True) and 'correct_answer' in feedback:
                st.markdown("#### Réponse attendue")
                st.info(f"```{feedback['correct_answer']}")
            
            # Show detailed explanation
            if 'explanation' in feedback:
                st.markdown("#### Explication")
                st.info(feedback['explanation'])
            
            # Show specific mistakes if any
            if 'mistakes' in feedback and feedback['mistakes']:
                st.markdown("#### Erreurs identifiées")
                for mistake in feedback['mistakes']:
                    st.error(f"- {mistake}")
    
    # Display personalized recommendations with resources
    st.markdown("### 📚 Recommandations personnalisées")
    
    if 'recommendations' in results and results['recommendations']:
        for i, rec in enumerate(results['recommendations'], 1):
            st.markdown(f"{i}. **{rec['topic']}**")
            st.write(rec['explanation'])
            
            # Show related resources if available
            if 'resources' in rec and rec['resources']:
                st.markdown("**Ressources recommandées :**")
                for resource in rec['resources']:
                    st.markdown(f"- [{resource['title']}]({resource['url']})")
            st.write("---")
    else:
        st.info("Aucune recommandation spécifique n'est disponible pour le moment.")
    
    # Add a button to start a new test
    st.markdown("---")
    if st.button("🔁 Commencer un nouveau test", type="primary", use_container_width=True):
        st.session_state.test_started = False
        st.rerun()

if __name__ == "__main__":
    main()
