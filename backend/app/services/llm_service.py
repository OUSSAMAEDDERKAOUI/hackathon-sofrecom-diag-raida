"""
LLM Service - OpenRouter Integration
Provides intelligent recommendations using free LLM models
"""

import requests
from flask import current_app
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class LLMService:
    """Service for interacting with OpenRouter LLM API"""
    
    @staticmethod
    def call_llm(
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        model: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Call OpenRouter LLM API with a prompt
        
        Args:
            prompt: The prompt to send to the LLM
            max_tokens: Maximum tokens in response (default from config)
            temperature: Sampling temperature (default from config)
            model: Model to use (default from config)
            
        Returns:
            Dict with 'success', 'response', and optional 'error' keys
        """
        try:
            # Get configuration
            api_key = current_app.config.get('OPENROUTER_API_KEY')
            base_url = current_app.config.get('OPENROUTER_BASE_URL')
            app_name = current_app.config.get('OPENROUTER_APP_NAME')
            site_url = current_app.config.get('OPENROUTER_SITE_URL')
            
            # Use provided values or fall back to config
            model = model or current_app.config.get('LLM_MODEL')
            max_tokens = max_tokens or current_app.config.get('LLM_MAX_TOKENS', 500)
            temperature = temperature or current_app.config.get('LLM_TEMPERATURE', 0.7)
            timeout = current_app.config.get('LLM_TIMEOUT', 30)
            
            # Check if API key is configured
            if not api_key:
                logger.warning("OpenRouter API key not configured")
                return {
                    'success': False,
                    'error': 'LLM API key not configured',
                    'fallback': True
                }
            
            # Prepare request
            url = f"{base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": site_url,
                "X-Title": app_name,
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": temperature
            }
            
            # Make API call
            logger.info(f"Calling LLM model: {model}")
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=timeout
            )
            
            # Check response
            if response.status_code == 200:
                data = response.json()
                content = data['choices'][0]['message']['content']
                
                logger.info("LLM call successful")
                return {
                    'success': True,
                    'response': content,
                    'model': model,
                    'tokens_used': data.get('usage', {})
                }
            else:
                logger.error(f"LLM API error: {response.status_code} - {response.text}")
                return {
                    'success': False,
                    'error': f"API returned status {response.status_code}",
                    'fallback': True
                }
                
        except requests.exceptions.Timeout:
            logger.error("LLM API timeout")
            return {
                'success': False,
                'error': 'Request timeout',
                'fallback': True
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"LLM API request error: {str(e)}")
            return {
                'success': False,
                'error': f'Request failed: {str(e)}',
                'fallback': True
            }
        except Exception as e:
            logger.error(f"Unexpected error in LLM call: {str(e)}")
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}',
                'fallback': True
            }
    
    @staticmethod
    def generate_recommendations(
        student_data: Dict[str, Any],
        analysis_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate personalized recommendations using LLM
        
        Args:
            student_data: Student information and responses
            analysis_results: Results from analysis service
            
        Returns:
            Dict with recommendations and metadata
        """
        from app.utils.prompts import create_recommendation_prompt
        
        # Create prompt from data
        prompt = create_recommendation_prompt(student_data, analysis_results)
        
        # Call LLM
        result = LLMService.call_llm(prompt)
        
        # Handle response
        if result['success']:
            return {
                'success': True,
                'recommendations': result['response'],
                'source': 'llm',
                'model': result.get('model'),
                'tokens_used': result.get('tokens_used')
            }
        else:
            # Use fallback if enabled
            if current_app.config.get('LLM_FALLBACK_ENABLED'):
                logger.info("Using fallback recommendations")
                from app.utils.fallback import generate_fallback_recommendations
                
                fallback_recs = generate_fallback_recommendations(
                    student_data,
                    analysis_results
                )
                
                return {
                    'success': True,
                    'recommendations': fallback_recs,
                    'source': 'fallback',
                    'reason': result.get('error')
                }
            else:
                return {
                    'success': False,
                    'error': result.get('error'),
                    'recommendations': None
                }


# Convenience function for direct use
def call_llm(prompt: str, **kwargs) -> Dict[str, Any]:
    """Convenience function to call LLM"""
    return LLMService.call_llm(prompt, **kwargs)


def generate_recommendations(
    student_data: Dict[str, Any],
    analysis_results: Dict[str, Any]
) -> Dict[str, Any]:
    """Convenience function to generate recommendations"""
    return LLMService.generate_recommendations(student_data, analysis_results)
