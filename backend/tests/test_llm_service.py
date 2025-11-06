"""
Tests for LLM Service
"""

import unittest
from unittest.mock import patch, Mock
from app.main import create_app
from app.services.llm_service import LLMService, call_llm


class TestLLMService(unittest.TestCase):
    """Test cases for LLM service"""
    
    def setUp(self):
        """Set up test client"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        """Clean up"""
        self.ctx.pop()
    
    @patch('app.services.llm_service.requests.post')
    def test_call_llm_success(self, mock_post):
        """Test successful LLM API call"""
        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Test recommendation'
                }
            }],
            'usage': {'total_tokens': 100}
        }
        mock_post.return_value = mock_response
        
        # Set API key in config
        self.app.config['OPENROUTER_API_KEY'] = 'test-key'
        
        # Call LLM
        result = call_llm("Test prompt")
        
        # Assertions
        self.assertTrue(result['success'])
        self.assertEqual(result['response'], 'Test recommendation')
        self.assertIn('tokens_used', result)
    
    def test_call_llm_no_api_key(self):
        """Test LLM call without API key"""
        # Remove API key
        self.app.config['OPENROUTER_API_KEY'] = None
        
        # Call LLM
        result = call_llm("Test prompt")
        
        # Assertions
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        self.assertTrue(result.get('fallback'))
    
    @patch('app.services.llm_service.requests.post')
    def test_call_llm_timeout(self, mock_post):
        """Test LLM call timeout"""
        # Mock timeout
        import requests
        mock_post.side_effect = requests.exceptions.Timeout()
        
        # Set API key
        self.app.config['OPENROUTER_API_KEY'] = 'test-key'
        
        # Call LLM
        result = call_llm("Test prompt")
        
        # Assertions
        self.assertFalse(result['success'])
        self.assertIn('timeout', result['error'].lower())
        self.assertTrue(result.get('fallback'))
    
    @patch('app.services.llm_service.requests.post')
    def test_call_llm_api_error(self, mock_post):
        """Test LLM API error response"""
        # Mock error response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = 'Internal server error'
        mock_post.return_value = mock_response
        
        # Set API key
        self.app.config['OPENROUTER_API_KEY'] = 'test-key'
        
        # Call LLM
        result = call_llm("Test prompt")
        
        # Assertions
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        self.assertTrue(result.get('fallback'))
    
    @patch('app.services.llm_service.LLMService.call_llm')
    def test_generate_recommendations_success(self, mock_call_llm):
        """Test successful recommendation generation"""
        # Mock LLM response
        mock_call_llm.return_value = {
            'success': True,
            'response': 'Personalized recommendations',
            'model': 'test-model',
            'tokens_used': {'total_tokens': 150}
        }
        
        # Test data
        student_data = {'student_id': '123'}
        analysis_results = {
            'weak_areas': ['algebra'],
            'accuracy': 0.75
        }
        
        # Generate recommendations
        result = LLMService.generate_recommendations(student_data, analysis_results)
        
        # Assertions
        self.assertTrue(result['success'])
        self.assertEqual(result['recommendations'], 'Personalized recommendations')
        self.assertEqual(result['source'], 'llm')
    
    @patch('app.services.llm_service.LLMService.call_llm')
    def test_generate_recommendations_fallback(self, mock_call_llm):
        """Test fallback recommendations when LLM fails"""
        # Mock LLM failure
        mock_call_llm.return_value = {
            'success': False,
            'error': 'API error',
            'fallback': True
        }
        
        # Enable fallback
        self.app.config['LLM_FALLBACK_ENABLED'] = True
        
        # Test data
        student_data = {'student_id': '123'}
        analysis_results = {
            'weak_areas': ['algebra'],
            'accuracy': 0.75
        }
        
        # Generate recommendations
        result = LLMService.generate_recommendations(student_data, analysis_results)
        
        # Assertions
        self.assertTrue(result['success'])
        self.assertEqual(result['source'], 'fallback')
        self.assertIn('recommendations', result)
    
    def test_custom_parameters(self):
        """Test LLM call with custom parameters"""
        # Set API key
        self.app.config['OPENROUTER_API_KEY'] = 'test-key'
        
        with patch('app.services.llm_service.requests.post') as mock_post:
            # Mock response
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'choices': [{'message': {'content': 'Test'}}],
                'usage': {}
            }
            mock_post.return_value = mock_response
            
            # Call with custom parameters
            call_llm(
                "Test prompt",
                max_tokens=300,
                temperature=0.5,
                model='custom-model'
            )
            
            # Check that custom parameters were used
            call_args = mock_post.call_args
            payload = call_args[1]['json']
            
            self.assertEqual(payload['max_tokens'], 300)
            self.assertEqual(payload['temperature'], 0.5)
            self.assertEqual(payload['model'], 'custom-model')


if __name__ == '__main__':
    unittest.main()
