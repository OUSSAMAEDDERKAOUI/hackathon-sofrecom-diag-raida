"""
Data models for the diagnostic system
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

@dataclass
class Question:
    """Represents a diagnostic question"""
    id: str
    text: str
    topic: str
    difficulty: DifficultyLevel
    options: List[Dict[str, Any]]  # List of {text: str, is_correct: bool, explanation: str}
    correct_answer: str
    explanation: str
    math_expression: Optional[str] = None  # For rendering math expressions
    image_url: Optional[str] = None  # For question images
    
@dataclass
class StudentResponse:
    """Represents a student's response to a question"""
    question_id: str
    answer: str
    is_correct: bool
    time_taken: float  # in seconds
    confidence: Optional[float] = None  # 0.0 to 1.0
    
@dataclass
class Student:
    """Represents a student taking the diagnostic"""
    student_id: str
    grade: int
    responses: List[StudentResponse] = field(default_factory=list)
    
@dataclass
class DiagnosticResult:
    """Results of a diagnostic assessment"""
    student_id: str
    total_questions: int
    correct_answers: int
    score: float  # 0.0 to 1.0
    weak_areas: List[str]
    strengths: List[str]
    difficulty_level: DifficultyLevel
    recommendations: List[Dict[str, Any]] = field(default_factory=list)
    
    @property
    def accuracy(self) -> float:
        return self.score
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "student_id": self.student_id,
            "total_questions": self.total_questions,
            "correct_answers": self.correct_answers,
            "score": self.score,
            "weak_areas": self.weak_areas,
            "strengths": self.strengths,
            "difficulty_level": self.difficulty_level.value,
            "recommendations": self.recommendations
        }
