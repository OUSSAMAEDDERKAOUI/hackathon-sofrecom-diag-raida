"""
Diagnostic Service
Handles diagnostic test generation and evaluation
"""
from typing import List, Dict, Any, Optional
import random
from datetime import datetime
from ..models.diagnostic_models import (
    Question, StudentResponse, Student, DiagnosticResult, 
    DifficultyLevel
)

class DiagnosticService:
    """Service for managing diagnostic tests and evaluations"""
    
    def __init__(self):
        self.questions: List[Question] = []
        self.load_sample_questions()
    
    def load_sample_questions(self) -> None:
        """Load sample diagnostic questions"""
        self.questions = [
            # Easy: Basic linear equations
            Question(
                id="q1",
                text="Résous l'équation: 2x + 3 = 7",
                topic="solving_equations",
                difficulty=DifficultyLevel.EASY,
                options=[
                    {"text": "x = 2", "is_correct": True, "explanation": "2(2) + 3 = 7"},
                    {"text": "x = 3", "is_correct": False, "explanation": "2(3) + 3 = 9 ≠ 7"},
                    {"text": "x = 4", "is_correct": False, "explanation": "2(4) + 3 = 11 ≠ 7"},
                ],
                correct_answer="x = 2",
                explanation="Soustrayez 3 des deux côtés: 2x = 4, puis divisez par 2: x = 2",
                math_expression="2x + 3 = 7"
            ),
            
            # Medium: Fractions
            Question(
                id="q2",
                text="Simplifie la fraction 12/18",
                topic="fractions",
                difficulty=DifficultyLevel.MEDIUM,
                options=[
                    {"text": "2/3", "is_correct": True, "explanation": "12 ÷ 6 = 2 et 18 ÷ 6 = 3"},
                    {"text": "3/4", "is_correct": False, "explanation": "Ce n'est pas la forme simplifiée de 12/18"},
                    {"text": "6/9", "is_correct": False, "explanation": "Peut être simplifiée davantage"},
                ],
                correct_answer="2/3",
                explanation="Le PGCD de 12 et 18 est 6. 12÷6=2 et 18÷6=3, donc 12/18 = 2/3",
                math_expression="\\frac{12}{18} = ?"
            ),
            
            # Hard: Quadratic equation
            Question(
                id="q3",
                text="Résous l'équation: x² - 5x + 6 = 0",
                topic="quadratic_equations",
                difficulty=DifficultyLevel.HARD,
                options=[
                    {"text": "x = 2, x = 3", "is_correct": True, "explanation": "(x-2)(x-3) = x² - 5x + 6"},
                    {"text": "x = -2, x = -3", "is_correct": False, "explanation": "(-2)² - 5(-2) + 6 = 4 + 10 + 6 = 20 ≠ 0"},
                    {"text": "x = 1, x = 6", "is_correct": False, "explanation": "(1)² - 5(1) + 6 = 2 ≠ 0 et (6)² - 5(6) + 6 = 12 ≠ 0"},
                ],
                correct_answer="x = 2, x = 3",
                explanation="L'équation se factorise en (x-2)(x-3)=0, donc les solutions sont x=2 et x=3",
                math_expression="x^2 - 5x + 6 = 0"
            ),
            
            # Geometry: Area of a circle
            Question(
                id="q4",
                text="Calcule l'aire d'un cercle de rayon 4 cm (prends π ≈ 3.14)",
                topic="geometry",
                difficulty=DifficultyLevel.MEDIUM,
                options=[
                    {"text": "50.24 cm²", "is_correct": True, "explanation": "A = πr² = 3.14 × 4² = 50.24"},
                    {"text": "25.12 cm²", "is_correct": False, "explanation": "C'est le périmètre (2πr), pas l'aire"},
                    {"text": "12.56 cm²", "is_correct": False, "explanation": "C'est l'aire d'un cercle de rayon 2 cm"},
                ],
                correct_answer="50.24 cm²",
                explanation="La formule de l'aire d'un cercle est A = πr². Ici, A = 3.14 × 4² = 50.24 cm²",
                math_expression="A = \\pi r^2, r = 4\\text{ cm}"
            ),
            
            # Word problem
            Question(
                id="q5",
                text="Si 5 stylos coûtent 7.50€, combien coûtent 8 stylos ?",
                topic="word_problems",
                difficulty=DifficultyLevel.EASY,
                options=[
                    {"text": "12.00€", "is_correct": True, "explanation": "1 stylo = 1.50€, donc 8 stylos = 12.00€"},
                    {"text": "10.50€", "is_correct": False, "explanation": "C'est le coût de 7 stylos"},
                    {"text": "15.00€", "is_correct": False, "explanation": "C'est le double du prix de 5 stylos"},
                ],
                correct_answer="12.00€",
                explanation="Prix d'un stylo = 7.50€ ÷ 5 = 1.50€. Donc 8 stylos = 8 × 1.50€ = 12.00€",
                math_expression="\\frac{7.50}{5} \\times 8 = ?"
            )
        ]
    
    def generate_diagnostic_test(self, num_questions: int = 5) -> List[Question]:
        """Generate a diagnostic test with random questions"""
        return random.sample(self.questions, min(num_questions, len(self.questions)))
    
    def evaluate_responses(
        self, 
        student_id: str, 
        responses: List[Dict[str, Any]]
    ) -> DiagnosticResult:
        """
        Evaluate student responses and generate diagnostic results
        
        Args:
            student_id: ID of the student
            responses: List of student responses
            
        Returns:
            DiagnosticResult with evaluation results
        """
        student_responses = []
        correct_answers = 0
        question_topics = set()
        correct_topics = set()
        
        for resp in responses:
            question = next((q for q in self.questions if q.id == resp["question_id"]), None)
            if not question:
                continue
                
            # Normalize answers for comparison (remove whitespace and convert to lowercase)
            student_answer = str(resp.get("answer", "")).strip().lower()
            correct_answer = str(question.correct_answer).strip().lower()
            
            # Check if answer is correct
            is_correct = student_answer == correct_answer
            if is_correct:
                correct_answers += 1
                correct_topics.add(question.topic)
                
            question_topics.add(question.topic)
            
            student_responses.append(
                StudentResponse(
                    question_id=resp["question_id"],
                    answer=resp["answer"],
                    is_correct=is_correct,
                    time_taken=resp.get("time_taken", 0),
                    confidence=resp.get("confidence")
                )
            )
        
        total_questions = len(student_responses)
        score = correct_answers / total_questions if total_questions > 0 else 0
        
        # Analyze performance by topic
        weak_areas = []
        strengths = []
        
        # If we have topic information, use it for analysis
        if question_topics:
            for topic in question_topics:
                topic_questions = [r for r in student_responses 
                                 if any(q.topic == topic for q in self.questions 
                                      if q.id == r.question_id)]
                topic_correct = sum(1 for r in topic_questions if r.is_correct)
                topic_score = topic_correct / len(topic_questions) if topic_questions else 0
                
                if topic_score < 0.5:  # Less than 50% correct in this topic
                    weak_areas.append(topic)
                elif topic_score >= 0.8:  # 80% or more correct
                    strengths.append(topic)
        
        # Fallback if no topic analysis was possible
        if not weak_areas and not strengths:
            if score < 0.5:
                weak_areas = ["solving_equations", "fractions"]
            if score >= 0.8:
                strengths = ["basic_arithmetic"]
        
        # Determine difficulty level based on score
        if score >= 0.8:
            difficulty = DifficultyLevel.HARD
        elif score >= 0.5:
            difficulty = DifficultyLevel.MEDIUM
        else:
            difficulty = DifficultyLevel.EASY
        
        # Generate recommendations based on performance
        recommendations = []
        if weak_areas:
            recommendations.append({
                "type": "focus_areas",
                "priority": "high",
                "suggestions": [
                    f"Pratiquez davantage les exercices sur: {', '.join(weak_areas)}",
                    "Utilisez des exercices progressifs pour renforcer ces compétences"
                ]
            })
        
        if strengths:
            recommendations.append({
                "type": "strengths",
                "priority": "info",
                "suggestions": [
                    f"Points forts identifiés: {', '.join(strengths)}",
                    "Utilisez ces compétences pour renforcer les domaines plus faibles"
                ]
            })
        
        return DiagnosticResult(
            student_id=student_id,
            total_questions=total_questions,
            correct_answers=correct_answers,
            score=score,
            weak_areas=weak_areas,
            strengths=strengths,
            difficulty_level=difficulty,
            recommendations=recommendations
        )
    
    def get_question_by_id(self, question_id: str) -> Optional[Question]:
        """Get a question by its ID"""
        return next((q for q in self.questions if q.id == question_id), None)
    
    def get_all_questions(self) -> List[Question]:
        """Get all available questions"""
        return self.questions

# Create a singleton instance
diagnostic_service = DiagnosticService()
