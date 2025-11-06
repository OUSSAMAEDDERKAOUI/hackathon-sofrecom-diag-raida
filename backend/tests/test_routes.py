import unittest
import json
from app.main import create_app


class TestRoutes(unittest.TestCase):
    """Test API routes"""
    
    def setUp(self):
        """Set up test client"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertIn('endpoints', data)
    
    def test_analysis_route(self):
        """Test analysis endpoint"""
        payload = {'test': 'data'}
        response = self.client.post(
            '/api/analysis/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_evaluation_route(self):
        """Test evaluation endpoint"""
        payload = {'test': 'data'}
        response = self.client.post(
            '/api/evaluation/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_recommendation_route(self):
        """Test recommendation endpoint"""
        payload = {
            'student_data': {
                'student_id': 'test_student_1',
                'grade': 8,
                'responses': [
                    {'question_id': 'q1', 'answer': '2x + 3 = 7', 'is_correct': True},
                    {'question_id': 'q2', 'answer': '3x - 5 = 10', 'is_correct': False}
                ]
            },
            'analysis_results': {
                'weak_areas': ['solving_equations', 'fractions'],
                'strengths': ['basic_arithmetic'],
                'accuracy': 0.75
            },
            'evaluation_results': {
                'score': 75,
                'total_questions': 4,
                'correct_answers': 3,
                'difficulty_level': 'intermediate'
            }
        }
        response = self.client.post(
            '/api/recommendation/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('recommendations', data)
    
    def test_404_error(self):
        """Test 404 error handler"""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()
