"""
Diagnostic Routes
Handles diagnostic test generation and submission
"""
from datetime import datetime
from flask import Blueprint, request, jsonify
from ..services.diagnostic_service import diagnostic_service
from ..models.diagnostic_models import Question, StudentResponse, DiagnosticResult
from typing import Dict, Any, List
import json

bp = Blueprint('diagnostic', __name__, url_prefix='/api/diagnostic')

@bp.route('/test', methods=['GET'])
def get_diagnostic_test():
    """
    Generate a diagnostic test
    Query params:
        - num_questions: Number of questions to include (default: 5)
    """
    try:
        num_questions = min(int(request.args.get('num_questions', 5)), 20)  # Max 20 questions
        questions = diagnostic_service.generate_diagnostic_test(num_questions)
        
        # Convert questions to dict for JSON serialization
        questions_data = []
        for q in questions:
            q_dict = {
                'id': q.id,
                'text': q.text,
                'topic': q.topic,
                'difficulty': q.difficulty.value,
                'options': [
                    {'text': opt['text'], 'explanation': opt['explanation']}
                    for opt in q.options
                ],
                'math_expression': q.math_expression,
                'image_url': q.image_url
            }
            questions_data.append(q_dict)
            
        return jsonify({
            'status': 'success',
            'test_id': f'diag_{len(questions)}_{int(datetime.now().timestamp())}',
            'questions': questions_data,
            'count': len(questions_data)
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@bp.route('/submit', methods=['POST'])
def submit_diagnostic():
    """
    Submit diagnostic test responses
    Body should include:
    {
        "student_id": "student123",
        "responses": [
            {
                "question_id": "q1",
                "answer": "x=2",
                "time_taken": 45.2,
                "confidence": 0.8
            },
            ...
        ]
    }
    """
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        responses = data.get('responses', [])
        
        if not student_id or not responses:
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields: student_id and responses are required'
            }), 400
        
        # Evaluate responses
        result = diagnostic_service.evaluate_responses(student_id, responses)
        
        # Convert result to dict
        result_data = {
            'student_id': result.student_id,
            'total_questions': result.total_questions,
            'correct_answers': result.correct_answers,
            'score': result.score,
            'weak_areas': result.weak_areas,
            'strengths': result.strengths,
            'difficulty_level': result.difficulty_level.value,
            'recommendations': result.recommendations
        }
        
        # In a real app, you might want to save this result to a database
        
        return jsonify({
            'status': 'success',
            'result': result_data
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error processing diagnostic: {str(e)}'
        }), 500

@bp.route('/question/<question_id>', methods=['GET'])
def get_question(question_id: str):
    """Get details for a specific question"""
    try:
        question = diagnostic_service.get_question_by_id(question_id)
        if not question:
            return jsonify({
                'status': 'error',
                'message': 'Question not found'
            }), 404
            
        # Don't include correct answer in the response
        question_data = {
            'id': question.id,
            'text': question.text,
            'topic': question.topic,
            'difficulty': question.difficulty.value,
            'options': [
                {'text': opt['text'], 'explanation': opt['explanation']}
                for opt in question.options
            ],
            'math_expression': question.math_expression,
            'image_url': question.image_url
        }
        
        return jsonify({
            'status': 'success',
            'question': question_data
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
