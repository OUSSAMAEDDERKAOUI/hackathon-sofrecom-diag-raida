# Guide d'intégration LLM pour Diag-Raida

## Vue d'ensemble

L'application utilise actuellement une analyse simulée (mock) des solutions des élèves. Ce guide explique comment intégrer un vrai LLM pour analyser les solutions mathématiques.

## Option 1 : OpenAI GPT (Recommandé)

### Installation

```bash
npm install openai
```

### Configuration

1. Créez un fichier `.env` à la racine :
```env
VITE_OPENAI_API_KEY=votre_clé_api_ici
```

2. Modifiez `/utils/llm-analyzer.ts` :

```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: import.meta.env.VITE_OPENAI_API_KEY,
  dangerouslyAllowBrowser: true // Pour le développement uniquement
});

export async function analyzeSolutionWithLLM(
  question: Question,
  solutionText: string
): Promise<LLMAnalysis> {
  
  const prompt = constructPrompt(question, solutionText);
  
  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4o', // ou 'gpt-4-turbo' ou 'gpt-3.5-turbo'
      messages: [
        {
          role: 'system',
          content: 'Tu es un professeur de mathématiques expert spécialisé dans l\'analyse pédagogique des solutions d\'élèves. Tu dois analyser le raisonnement mathématique, identifier les erreurs et donner des conseils constructifs.'
        },
        {
          role: 'user',
          content: prompt
        }
      ],
      temperature: 0.3,
      response_format: { type: 'json_object' }
    });

    const content = response.choices[0].message.content;
    if (!content) throw new Error('No response from LLM');
    
    return JSON.parse(content) as LLMAnalysis;
    
  } catch (error) {
    console.error('Error calling OpenAI:', error);
    // Fallback vers l'analyse mock
    return mockLLMAnalysis(question, solutionText);
  }
}
```

### Prompt optimisé

Le prompt dans `constructPrompt()` doit être modifié pour demander explicitement un JSON :

```typescript
function constructPrompt(question: Question, solutionText: string): string {
  return `Analyse cette solution mathématique d'un élève.

QUESTION: ${question.question}
CONTEXTE: ${question.context}
COMPÉTENCE: ${question.skill}
RÉPONSE ATTENDUE: ${question.correctAnswer}

SOLUTION DE L'ÉLÈVE:
${solutionText}

Analyse la solution en vérifiant :
1. La correction de la réponse finale
2. La validité de chaque étape du raisonnement
3. Les erreurs de calcul, de signe, de méthode
4. Les points forts du raisonnement
5. Les domaines à améliorer

IMPORTANT: Réponds UNIQUEMENT avec un objet JSON (pas de texte avant ou après) ayant cette structure exacte:
{
  "isCorrect": true ou false (la réponse finale est-elle correcte?),
  "correctAnswers": ["liste", "des", "réponses", "attendues"],
  "stepsCorrect": true ou false (le raisonnement est-il correct?),
  "errors": [
    {
      "step": "l'étape erronée (copie exacte)",
      "issue": "description claire du problème",
      "correction": "explication de la correction"
    }
  ],
  "feedback": "commentaire général en 1-2 phrases",
  "strengths": ["liste", "des", "points", "forts"],
  "areasToImprove": ["liste", "des", "points", "à", "améliorer"]
}`;
}
```

## Option 2 : Anthropic Claude

```bash
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: import.meta.env.VITE_ANTHROPIC_API_KEY,
});

export async function analyzeSolutionWithLLM(
  question: Question,
  solutionText: string
): Promise<LLMAnalysis> {
  
  const prompt = constructPrompt(question, solutionText);
  
  try {
    const message = await anthropic.messages.create({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 1024,
      messages: [
        {
          role: 'user',
          content: prompt
        }
      ],
    });

    const content = message.content[0];
    if (content.type !== 'text') throw new Error('Unexpected response type');
    
    // Extraire le JSON de la réponse
    const jsonMatch = content.text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) throw new Error('No JSON found in response');
    
    return JSON.parse(jsonMatch[0]) as LLMAnalysis;
    
  } catch (error) {
    console.error('Error calling Claude:', error);
    return mockLLMAnalysis(question, solutionText);
  }
}
```

## Option 3 : Backend personnalisé (Production)

Pour une vraie application en production, il est recommandé d'avoir un backend :

### Structure

```
backend/
  ├── server.js
  ├── routes/
  │   └── analyze.js
  └── services/
      └── llm-service.js
```

### Exemple avec Express.js

```javascript
// backend/server.js
import express from 'express';
import cors from 'cors';
import analyzeRoute from './routes/analyze.js';

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/analyze', analyzeRoute);

app.listen(3001, () => {
  console.log('Backend running on port 3001');
});

// backend/routes/analyze.js
export default async function analyzeRoute(req, res) {
  const { question, solutionText } = req.body;
  
  try {
    const analysis = await analyzeSolutionWithBackendLLM(question, solutionText);
    res.json(analysis);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Analysis failed' });
  }
}
```

### Modification frontend

```typescript
// utils/llm-analyzer.ts
export async function analyzeSolutionWithLLM(
  question: Question,
  solutionText: string
): Promise<LLMAnalysis> {
  
  try {
    const response = await fetch('http://localhost:3001/api/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question, solutionText })
    });

    if (!response.ok) throw new Error('API request failed');
    
    return await response.json();
    
  } catch (error) {
    console.error('Error calling backend:', error);
    return mockLLMAnalysis(question, solutionText);
  }
}
```

## Conseils de sécurité

### ⚠️ NE JAMAIS :
- Exposer votre clé API dans le code frontend en production
- Commiter les fichiers `.env` dans Git
- Utiliser `dangerouslyAllowBrowser: true` en production

### ✅ TOUJOURS :
- Utiliser un backend pour gérer les appels API en production
- Limiter le nombre de requêtes (rate limiting)
- Valider les entrées utilisateur
- Gérer les erreurs avec des fallbacks
- Monitorer les coûts d'API

## Coûts estimés

### OpenAI GPT-4o :
- ~$0.005 par question (avec prompt optimisé)
- Pour 100 élèves × 5 questions = $2.50

### OpenAI GPT-3.5-turbo :
- ~$0.001 par question
- Pour 100 élèves × 5 questions = $0.50

### Claude 3.5 Sonnet :
- ~$0.003 par question
- Pour 100 élèves × 5 questions = $1.50

## Optimisations

1. **Cache** : Mémoriser les analyses pour des solutions identiques
2. **Batch processing** : Analyser plusieurs solutions en une fois
3. **Modèle plus petit** : Utiliser GPT-3.5 pour réduire les coûts
4. **Validation locale** : Vérifier d'abord avec des règles simples avant d'appeler le LLM

## Test

Pour tester sans API :
- L'application utilise déjà `mockLLMAnalysis()` comme fallback
- Modifiez les patterns dans le mock pour tester différents scénarios
- Utilisez des variables d'environnement pour basculer entre mock et API réelle

## Support

Pour plus d'aide sur l'intégration :
- OpenAI : https://platform.openai.com/docs
- Anthropic : https://docs.anthropic.com
- Figma Make : Documentation interne
