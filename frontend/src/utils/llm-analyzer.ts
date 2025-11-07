import { Question, LLMAnalysis } from '../types';

// This function would call an actual LLM API in production
// For now, it provides a structured mock response
export async function analyzeSolutionWithLLM(
  question: Question,
  solutionText: string
): Promise<LLMAnalysis> {
  
  // In production, you would call OpenAI or another LLM API
  // Example prompt structure for the LLM:
  const prompt = constructPrompt(question, solutionText);
  
  // TODO: Replace with actual LLM API call
  // const response = await callLLMAPI(prompt);
  // return parseLLMResponse(response);
  
  // Mock analysis for demonstration
  return mockLLMAnalysis(question, solutionText);
}

function constructPrompt(question: Question, solutionText: string): string {
  return `Tu es un professeur de mathématiques expert. Analyse la solution suivante d'un élève.

QUESTION:
${question.question}

CONTEXTE:
${question.context || 'Équation du premier degré'}

COMPÉTENCE ÉVALUÉE:
${question.skill}

SOLUTION DE L'ÉLÈVE:
${solutionText}

INSTRUCTIONS D'ANALYSE:
1. Vérifie si la solution finale est correcte (réponse(s) attendue(s): ${question.correctAnswer})
2. Analyse chaque étape du raisonnement
3. Identifie les erreurs spécifiques (calcul, signe, méthode, etc.)
4. Note les points forts du raisonnement
5. Suggère des améliorations

RÉPONDS AU FORMAT JSON:
{
  "isCorrect": boolean,
  "correctAnswers": ["liste", "des", "réponses", "correctes"],
  "stepsCorrect": boolean,
  "errors": [
    {
      "step": "l'étape erronée",
      "issue": "description du problème",
      "correction": "comment corriger"
    }
  ],
  "feedback": "commentaire général",
  "strengths": ["points forts"],
  "areasToImprove": ["points à améliorer"]
}`;
}

// Mock LLM analysis - simulates what an LLM would return
function mockLLMAnalysis(question: Question, solutionText: string): LLMAnalysis {
  const lowerSolution = solutionText.toLowerCase();
  
  // Extract numbers from solution
  const numbers = solutionText.match(/-?\d+\.?\d*/g) || [];
  const finalAnswers = extractFinalAnswers(solutionText);
  
  // Check if correct answer is present
  const correctAnswers = question.correctAnswer.split(',').map(a => a.trim());
  const hasCorrectAnswer = correctAnswers.some(ans => 
    finalAnswers.some(userAns => Math.abs(parseFloat(userAns) - parseFloat(ans)) < 0.01)
  );
  
  // Analyze based on question type
  if (question.id === 'q5') {
    // Product equation - special case
    return analyzeProductEquation(question, solutionText, finalAnswers);
  }
  
  // Check for common patterns
  const hasSteps = solutionText.includes('=') && solutionText.split('\n').length > 2;
  const showsWork = /(-?\d+x|\dx)/.test(lowerSolution);
  const hasExplanation = lowerSolution.includes('soit') || 
                         lowerSolution.includes('donc') || 
                         lowerSolution.includes('alors');
  
  const errors: LLMAnalysis['errors'] = [];
  const strengths: string[] = [];
  const areasToImprove: string[] = [];
  
  // Analyze strengths
  if (hasSteps) {
    strengths.push('Présentation claire avec étapes détaillées');
  }
  if (hasExplanation) {
    strengths.push('Explications en langage naturel présentes');
  }
  if (showsWork) {
    strengths.push('Raisonnement algébrique visible');
  }
  
  // Check for specific errors
  if (!hasCorrectAnswer) {
    // Try to identify the type of error
    if (numbers.length > 0) {
      const userAnswer = numbers[numbers.length - 1];
      const expectedAnswer = parseFloat(correctAnswers[0]);
      
      // Check common error patterns
      if (Math.abs(parseFloat(userAnswer) - expectedAnswer * 2) < 0.01) {
        errors.push({
          step: `x = ${userAnswer}`,
          issue: 'Oubli de diviser par le coefficient',
          correction: `Il faut diviser par le coefficient de x. La bonne réponse est x = ${correctAnswers[0]}`
        });
        areasToImprove.push('Bien penser à diviser par le coefficient de x à la fin');
      } else if (Math.abs(parseFloat(userAnswer) + expectedAnswer) < 0.01) {
        errors.push({
          step: `x = ${userAnswer}`,
          issue: 'Erreur de signe',
          correction: `Attention au signe lors des opérations. La bonne réponse est x = ${correctAnswers[0]}`
        });
        areasToImprove.push('Revoir les règles des signes lors des opérations');
      } else {
        errors.push({
          step: `x = ${userAnswer}`,
          issue: 'Résultat final incorrect',
          correction: `Vérifiez vos calculs. La bonne réponse est x = ${correctAnswers[0]}`
        });
        areasToImprove.push('Vérifier chaque étape de calcul');
      }
    } else {
      errors.push({
        step: 'Solution complète',
        issue: 'Solution non trouvée ou illisible',
        correction: `Essayez d'isoler x étape par étape. La réponse est x = ${correctAnswers[0]}`
      });
      areasToImprove.push('Écrire clairement la solution finale sous forme x = valeur');
    }
  }
  
  // Check if steps are shown
  if (!hasSteps) {
    areasToImprove.push('Montrer les étapes intermédiaires du raisonnement');
  }
  
  return {
    isCorrect: hasCorrectAnswer,
    correctAnswers,
    stepsCorrect: hasSteps && hasCorrectAnswer,
    errors,
    feedback: hasCorrectAnswer 
      ? 'Excellente solution ! Le résultat est correct.'
      : 'La solution nécessite quelques corrections. Vérifie les étapes ci-dessous.',
    strengths,
    areasToImprove
  };
}

function analyzeProductEquation(
  question: Question, 
  solutionText: string, 
  finalAnswers: string[]
): LLMAnalysis {
  const errors: LLMAnalysis['errors'] = [];
  const strengths: string[] = [];
  const areasToImprove: string[] = [];
  
  // Expected answers
  const expected = ['-3/2', '-1.5', '3/7', '0.42857', '0.43'];
  
  // Check if student recognized the product form
  const mentionsProduct = /produit|facteur|nul/i.test(solutionText);
  const hasTwoSolutions = finalAnswers.length >= 2;
  const hasOr = /\bou\b/i.test(solutionText);
  
  if (mentionsProduct) {
    strengths.push('Reconnaissance correcte de l\'équation produit');
  }
  
  if (hasOr || hasTwoSolutions) {
    strengths.push('Compréhension qu\'il y a plusieurs solutions');
  }
  
  // Check if both solutions are present
  const hasFirstSolution = finalAnswers.some(ans => 
    Math.abs(parseFloat(ans) - (-1.5)) < 0.1
  );
  const hasSecondSolution = finalAnswers.some(ans => 
    Math.abs(parseFloat(ans) - (3/7)) < 0.1
  );
  
  if (!mentionsProduct) {
    errors.push({
      step: 'Début de résolution',
      issue: 'Équation produit non reconnue',
      correction: 'Si un produit de facteurs est nul, alors l\'un au moins des facteurs est nul'
    });
    areasToImprove.push('Reconnaître les équations produit');
  }
  
  if (!hasTwoSolutions) {
    errors.push({
      step: 'Solutions',
      issue: 'Une seule solution trouvée',
      correction: 'Cette équation a deux solutions : x = -3/2 et x = 3/7'
    });
    areasToImprove.push('Chercher toutes les solutions possibles');
  }
  
  if (!hasFirstSolution) {
    errors.push({
      step: '4x + 6 = 0',
      issue: 'Première solution incorrecte ou manquante',
      correction: 'De 4x + 6 = 0, on obtient x = -6/4 = -3/2'
    });
  }
  
  if (!hasSecondSolution) {
    errors.push({
      step: '3 - 7x = 0',
      issue: 'Deuxième solution incorrecte ou manquante',
      correction: 'De 3 - 7x = 0, on obtient x = 3/7'
    });
  }
  
  const isCorrect = hasFirstSolution && hasSecondSolution;
  
  return {
    isCorrect,
    correctAnswers: ['-3/2', '3/7'],
    stepsCorrect: isCorrect && mentionsProduct,
    errors,
    feedback: isCorrect
      ? 'Parfait ! Les deux solutions ont été trouvées.'
      : 'Cette équation produit nécessite de trouver deux solutions.',
    strengths,
    areasToImprove
  };
}

function extractFinalAnswers(text: string): string[] {
  const answers: string[] = [];
  
  // Look for x = value patterns
  const xEquals = text.matchAll(/x\s*=\s*(-?\d+\.?\d*(?:\/\d+)?)/gi);
  for (const match of xEquals) {
    answers.push(match[1]);
  }
  
  // Look for fractions
  const fractions = text.matchAll(/(-?\d+)\s*\/\s*(\d+)/g);
  for (const match of fractions) {
    const value = parseFloat(match[1]) / parseFloat(match[2]);
    answers.push(value.toString());
  }
  
  return answers;
}

// Placeholder for actual LLM API call
async function callLLMAPI(prompt: string): Promise<string> {
  // TODO: Implement actual API call
  // Example with OpenAI:
  /*
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'Tu es un professeur de mathématiques expert.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.3
    })
  });
  
  const data = await response.json();
  return data.choices[0].message.content;
  */
  
  throw new Error('LLM API not configured');
}
