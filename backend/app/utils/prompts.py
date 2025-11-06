"""
Prompt Templates for LLM
Creates structured prompts for different use cases
"""

from typing import Dict, Any


def create_recommendation_prompt(
    student_data: Dict[str, Any],
    analysis_results: Dict[str, Any]
) -> str:
    """
    Create a prompt for generating personalized math recommendations
    
    Args:
        student_data: Student information and responses
        analysis_results: Analysis results including weak areas
        
    Returns:
        Formatted prompt string
    """
    # Extract key information
    weak_areas = analysis_results.get('weak_areas', [])
    accuracy = analysis_results.get('accuracy', 0)
    difficulty_level = analysis_results.get('difficulty_level', 'intermediate')
    
    # Build prompt
    prompt = f"""Tu es un assistant pédagogique spécialisé en mathématiques pour les élèves du collège.

Contexte de l'élève:
- Niveau de précision: {accuracy:.1%}
- Niveau de difficulté: {difficulty_level}
- Domaines à améliorer: {', '.join(weak_areas) if weak_areas else 'Aucun identifié'}

Tâche:
Génère des recommandations personnalisées et encourageantes pour aider cet élève à progresser en mathématiques.

Tes recommandations doivent inclure:
1. Un message d'encouragement adapté au niveau de l'élève
2. 3-4 conseils spécifiques pour améliorer les domaines faibles
3. Des suggestions d'exercices ou de ressources appropriées
4. Une stratégie d'apprentissage progressive

Format ta réponse de manière claire et structurée. Sois positif, encourageant et constructif.
Adapte ton langage au niveau collège (12-15 ans).

Recommandations:"""

    return prompt


def create_exercise_suggestion_prompt(
    topic: str,
    difficulty: str,
    student_level: str
) -> str:
    """
    Create a prompt for suggesting practice exercises
    
    Args:
        topic: Math topic (e.g., "algebra", "geometry")
        difficulty: Difficulty level
        student_level: Student's current level
        
    Returns:
        Formatted prompt string
    """
    prompt = f"""Suggère 3 exercices de mathématiques sur le thème "{topic}" 
pour un élève de niveau {student_level} avec une difficulté {difficulty}.

Pour chaque exercice, fournis:
1. L'énoncé clair et précis
2. Le niveau de difficulté
3. Les concepts mathématiques travaillés
4. Un indice pour aider l'élève

Format ta réponse de manière structurée et pédagogique."""

    return prompt


def create_concept_explanation_prompt(
    concept: str,
    student_level: str
) -> str:
    """
    Create a prompt for explaining a math concept
    
    Args:
        concept: Math concept to explain
        student_level: Student's level
        
    Returns:
        Formatted prompt string
    """
    prompt = f"""Explique le concept mathématique "{concept}" à un élève de niveau {student_level}.

Ton explication doit:
1. Être claire et accessible
2. Utiliser des exemples concrets
3. Inclure une analogie ou métaphore si pertinent
4. Proposer un exemple d'application pratique

Limite ton explication à 150-200 mots. Sois pédagogique et encourageant."""

    return prompt


def create_error_analysis_prompt(
    question: str,
    student_answer: str,
    correct_answer: str
) -> str:
    """
    Create a prompt for analyzing student errors
    
    Args:
        question: The question asked
        student_answer: Student's answer
        correct_answer: Correct answer
        
    Returns:
        Formatted prompt string
    """
    prompt = f"""Analyse l'erreur de l'élève dans cet exercice de mathématiques.

Question: {question}
Réponse de l'élève: {student_answer}
Réponse correcte: {correct_answer}

Fournis:
1. Une identification du type d'erreur (conceptuelle, calcul, méthode, etc.)
2. Une explication de pourquoi la réponse est incorrecte
3. Des conseils pour éviter cette erreur à l'avenir
4. Un rappel du concept ou de la méthode correcte

Sois bienveillant et constructif dans ton analyse."""

    return prompt


def create_study_plan_prompt(
    weak_areas: list,
    time_available: str,
    goals: str
) -> str:
    """
    Create a prompt for generating a study plan
    
    Args:
        weak_areas: List of areas to improve
        time_available: Available study time
        goals: Student's goals
        
    Returns:
        Formatted prompt string
    """
    prompt = f"""Crée un plan d'étude personnalisé en mathématiques.

Domaines à améliorer: {', '.join(weak_areas)}
Temps disponible: {time_available}
Objectifs: {goals}

Le plan doit inclure:
1. Une répartition hebdomadaire du temps d'étude
2. Des objectifs spécifiques pour chaque domaine
3. Des ressources recommandées (types d'exercices, concepts à réviser)
4. Des jalons pour mesurer les progrès
5. Des conseils pour rester motivé

Sois réaliste et adapte le plan au temps disponible."""

    return prompt
