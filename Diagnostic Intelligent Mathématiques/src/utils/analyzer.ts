import { Question, Answer, DiagnosticResult, ErrorAnalysis, RemediationPlan } from '../types';
import { resourceDatabase } from '../data/resources';
import { analyzeSolutionWithLLM } from './llm-analyzer';

export async function analyzeAnswers(questions: Question[], answers: Answer[]): Promise<DiagnosticResult> {
  const correctAnswers = answers.filter(a => a.isCorrect).length;
  const skillsMastered: string[] = [];
  const skillsToImprove: string[] = [];
  const errors: ErrorAnalysis[] = [];

  questions.forEach((question, index) => {
    const answer = answers[index];
    
    if (answer.isCorrect) {
      if (!skillsMastered.includes(question.skill)) {
        skillsMastered.push(question.skill);
      }
    } else {
      if (!skillsToImprove.includes(question.skill)) {
        skillsToImprove.push(question.skill);
      }
      
      // Convert LLM analysis to error analysis
      if (answer.llmAnalysis) {
        const errorAnalysis: ErrorAnalysis = {
          skill: question.skill,
          errorType: answer.llmAnalysis.errors.length > 0 
            ? answer.llmAnalysis.errors[0].issue 
            : 'Erreur de raisonnement',
          description: answer.llmAnalysis.feedback,
          recommendation: answer.llmAnalysis.areasToImprove.length > 0
            ? answer.llmAnalysis.areasToImprove.join('. ')
            : 'Revoir les bases de cette compétence',
          specificErrors: answer.llmAnalysis.errors,
          strengths: answer.llmAnalysis.strengths
        };
        errors.push(errorAnalysis);
      }
    }
  });

  return {
    totalQuestions: questions.length,
    correctAnswers,
    skillsMastered,
    skillsToImprove,
    errors
  };
}

export function generateRemediationPlan(diagnostic: DiagnosticResult): RemediationPlan {
  const resources = diagnostic.skillsToImprove.flatMap(skill => {
    return resourceDatabase[skill] || [];
  });

  // Remove duplicates and prioritize by difficulty
  const uniqueResources = Array.from(
    new Map(resources.map(r => [r.title, r])).values()
  );

  return {
    skills: diagnostic.skillsToImprove,
    resources: uniqueResources
  };
}
