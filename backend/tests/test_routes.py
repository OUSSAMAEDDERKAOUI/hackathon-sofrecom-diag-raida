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
        payload = {'test': 'data'}
        response = self.client.post(
            '/api/recommendation/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_404_error(self):
        """Test 404 error handler"""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()
