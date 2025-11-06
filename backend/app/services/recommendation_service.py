"""
Recommendation Service
Generates personalized learning recommendations using LLM
"""

from typing import Dict, Any
from app.services.llm_service import generate_recommendations as llm_generate_recommendations
import logging

logger = logging.getLogger(__name__)


def generate_recommendations(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate personalized recommendations based on evaluation
    
    Args:
        data: Dictionary containing:
            - student_data: Student information and responses
            - analysis_results: Results from analysis service
            - evaluation_results: Results from evaluation service
            
    Returns:
        Dictionary with recommendations and metadata
    """
    try:
        # Validate input
        if not data:
            return {
                'status': 'failed',
                'error': 'No data provided'
            }
        
        # Extract required data
        student_data = data.get('student_data', {})
        analysis_results = data.get('analysis_results', {})
        evaluation_results = data.get('evaluation_results', {})
        
        # Validate required fields
        if not student_data and not analysis_results:
            return {
                'status': 'failed',
                'error': 'Missing required data (student_data or analysis_results)'
            }
        
        # Merge analysis and evaluation results for comprehensive recommendations
        combined_results = {
            **analysis_results,
            **evaluation_results
        }
        
        # Generate recommendations using LLM
        logger.info("Generating recommendations with LLM")
        llm_result = llm_generate_recommendations(student_data, combined_results)
        
        if llm_result['success']:
            return {
                'status': 'success',
                'recommendations': llm_result['recommendations'],
                'source': llm_result.get('source', 'llm'),
                'model': llm_result.get('model'),
                'metadata': {
                    'tokens_used': llm_result.get('tokens_used'),
                    'weak_areas': combined_results.get('weak_areas', []),
                    'accuracy': combined_results.get('accuracy', 0),
                    'difficulty_level': combined_results.get('difficulty_level', 'intermediate')
                }
            }
        else:
            return {
                'status': 'failed',
                'error': llm_result.get('error', 'Failed to generate recommendations'),
                'recommendations': llm_result.get('recommendations')
            }
            
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        return {
            'status': 'failed',
            'error': f'Unexpected error: {str(e)}'
        }
