"""
Test script to verify LLM service functionality
"""
import os
import sys
import json
from dotenv import load_dotenv

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()

from app.services.llm_service import LLMService

def test_llm_service():
    """Test the LLM service with a simple prompt"""
    print("Testing LLM service...")
    
    # Test data
    test_prompt = "You are a helpful math tutor. Provide a brief explanation of how to solve a simple linear equation like 2x + 3 = 7."
    
    # Call the LLM service
    print(f"Sending prompt to LLM: {test_prompt[:100]}...")
    result = LLMService.call_llm(test_prompt, max_tokens=200)
    
    # Print the result
    print("\nLLM Response:")
    print(json.dumps(result, indent=2))
    
    # Check if the response is successful
    if result.get('success'):
        print("\n✅ LLM service is working correctly!")
    else:
        print(f"\n❌ LLM service returned an error: {result.get('error', 'Unknown error')}")
        if 'fallback' in result:
            print("Note: Make sure to set the OPENROUTER_API_KEY in your .env file")

if __name__ == "__main__":
    test_llm_service()
