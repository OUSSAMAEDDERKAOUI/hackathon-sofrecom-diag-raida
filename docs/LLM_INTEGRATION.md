## 🤖 LLM Integration Guide

## Overview

Diag-Raida uses **OpenRouter** to access free LLM models for generating intelligent, personalized math recommendations.

---

## 🆓 Free Models Available

### **Recommended Models:**

1. **meta-llama/llama-3.2-3b-instruct:free** (Default)
   - Fast and efficient
   - Good for quick recommendations
   - Best for production use

2. **google/gemma-2-9b-it:free**
   - Higher quality responses
   - Better understanding of context
   - Slightly slower

3. **mistralai/mistral-7b-instruct:free**
   - Balanced performance
   - Good multilingual support
   - Reliable

4. **microsoft/phi-3-mini-128k-instruct:free**
   - Very long context window
   - Good for detailed analysis
   - Excellent for complex prompts

5. **qwen/qwen-2-7b-instruct:free**
   - Strong multilingual capabilities
   - Good for French language
   - Balanced performance

---

## 🚀 Setup

### Step 1: Get OpenRouter API Key

1. Go to [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up for a free account
3. Create an API key
4. Copy the key

### Step 2: Configure Environment

```bash
cd backend
cp .env.example .env
```

Edit `.env`:
```bash
OPENROUTER_API_KEY=your-actual-api-key-here
LLM_MODEL=meta-llama/llama-3.2-3b-instruct:free
```

### Step 3: Install Dependencies

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 4: Test

```bash
python3 -c "from app.main import create_app; app = create_app(); print('✅ LLM configured')"
```

---

## 📝 Usage

### Basic LLM Call

```python
from app.services.llm_service import call_llm

# Simple call
result = call_llm("Explain algebra to a 7th grader")

if result['success']:
    print(result['response'])
else:
    print(f"Error: {result['error']}")
```

### Generate Recommendations

```python
from app.services.llm_service import generate_recommendations

student_data = {
    'student_id': '123',
    'grade': 7
}

analysis_results = {
    'weak_areas': ['algebra', 'fractions'],
    'accuracy': 0.65,
    'difficulty_level': 'intermediate'
}

result = generate_recommendations(student_data, analysis_results)

if result['success']:
    print(result['recommendations'])
    print(f"Source: {result['source']}")  # 'llm' or 'fallback'
```

### Custom Parameters

```python
result = call_llm(
    prompt="Your prompt here",
    max_tokens=300,
    temperature=0.5,
    model='google/gemma-2-9b-it:free'
)
```

---

## 🎯 Prompt Templates

### Available Templates

Located in `app/utils/prompts.py`:

1. **`create_recommendation_prompt`** - Personalized recommendations
2. **`create_exercise_suggestion_prompt`** - Practice exercises
3. **`create_concept_explanation_prompt`** - Concept explanations
4. **`create_error_analysis_prompt`** - Error analysis
5. **`create_study_plan_prompt`** - Study plans

### Example Usage

```python
from app.utils.prompts import create_recommendation_prompt

prompt = create_recommendation_prompt(student_data, analysis_results)
result = call_llm(prompt)
```

---

## 🛡️ Fallback System

When LLM is unavailable (no API key, timeout, error), the system automatically uses rule-based fallback recommendations.

### Fallback Features:

- ✅ Rule-based recommendations
- ✅ Area-specific tips
- ✅ General study advice
- ✅ Next steps guidance
- ✅ No API required

### Configuration

```python
# In config.py
LLM_FALLBACK_ENABLED = True  # Enable fallback (default)
```

---

## 🔧 Configuration Options

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=your-key

# Optional
LLM_MODEL=meta-llama/llama-3.2-3b-instruct:free
OPENROUTER_SITE_URL=http://localhost:5000
```

### Config.py Settings

```python
# Timeout for API calls
LLM_TIMEOUT = 30  # seconds

# Maximum tokens in response
LLM_MAX_TOKENS = 500

# Sampling temperature (0.0 - 1.0)
LLM_TEMPERATURE = 0.7

# Enable fallback recommendations
LLM_FALLBACK_ENABLED = True
```

---

## 📊 API Response Format

### Successful Response

```json
{
  "success": true,
  "response": "Personalized recommendations text...",
  "model": "meta-llama/llama-3.2-3b-instruct:free",
  "tokens_used": {
    "prompt_tokens": 150,
    "completion_tokens": 200,
    "total_tokens": 350
  }
}
```

### Error Response (with Fallback)

```json
{
  "success": true,
  "recommendations": "Rule-based recommendations...",
  "source": "fallback",
  "reason": "API timeout"
}
```

### Error Response (no Fallback)

```json
{
  "success": false,
  "error": "API key not configured",
  "fallback": true
}
```

---

## 🧪 Testing

### Unit Tests

```bash
cd backend
pytest tests/test_llm_service.py -v
```

### Manual Testing

```bash
# Test with mock data
python3 -c "
from app.main import create_app
from app.services.llm_service import call_llm

app = create_app()
with app.app_context():
    result = call_llm('Test prompt')
    print(result)
"
```

### Test Fallback

```bash
# Remove API key to test fallback
unset OPENROUTER_API_KEY
python3 test_fallback.py
```

---

## 🎨 Customization

### Add New Prompt Template

Edit `app/utils/prompts.py`:

```python
def create_custom_prompt(data):
    """Your custom prompt"""
    prompt = f"""
    Your custom prompt template here
    Data: {data}
    """
    return prompt
```

### Add New Fallback Logic

Edit `app/utils/fallback.py`:

```python
def custom_fallback_logic(data):
    """Your custom fallback logic"""
    # Your logic here
    return recommendations
```

---

## 📈 Best Practices

### 1. Prompt Engineering

- ✅ Be specific and clear
- ✅ Provide context
- ✅ Use structured format
- ✅ Include examples if needed
- ✅ Set clear expectations

### 2. Error Handling

- ✅ Always check `result['success']`
- ✅ Handle fallback gracefully
- ✅ Log errors for debugging
- ✅ Provide user-friendly messages

### 3. Performance

- ✅ Use appropriate `max_tokens`
- ✅ Set reasonable timeout
- ✅ Cache responses when possible
- ✅ Use faster models for simple tasks

### 4. Cost Management

- ✅ Use free models
- ✅ Optimize prompts (fewer tokens)
- ✅ Enable fallback
- ✅ Monitor usage

---

## 🐛 Troubleshooting

### Issue: "API key not configured"

**Solution:**
```bash
# Check .env file
cat backend/.env | grep OPENROUTER

# Set environment variable
export OPENROUTER_API_KEY=your-key
```

### Issue: "Request timeout"

**Solutions:**
- Increase timeout in config
- Use faster model
- Reduce max_tokens
- Check internet connection

### Issue: "API error 429 (Rate limit)"

**Solutions:**
- Wait a few seconds
- Use different model
- Implement request queuing
- Use fallback

### Issue: "Poor quality responses"

**Solutions:**
- Improve prompt clarity
- Try different model
- Adjust temperature
- Provide more context

---

## 📚 Resources

- **OpenRouter Docs:** https://openrouter.ai/docs
- **Model Comparison:** https://openrouter.ai/models
- **API Reference:** https://openrouter.ai/docs/api-reference
- **Free Models:** https://openrouter.ai/models?free=true

---

## ✅ Checklist

Before deploying:

- [ ] API key configured
- [ ] Environment variables set
- [ ] Dependencies installed
- [ ] Tests passing
- [ ] Fallback tested
- [ ] Error handling verified
- [ ] Prompts optimized
- [ ] Documentation updated

---

## 🎉 Summary

**LLM Integration provides:**
- ✅ Intelligent recommendations
- ✅ Personalized suggestions
- ✅ Multiple free models
- ✅ Automatic fallback
- ✅ Easy to use
- ✅ Well tested

**Get your API key and start generating smart recommendations!** 🚀
