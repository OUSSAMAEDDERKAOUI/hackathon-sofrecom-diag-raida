export interface Question {
  id: string;
  question: string;
  correctAnswer: string;
  skill: string;
  context?: string;
}

export interface Answer {
  questionId: string;
  solutionText: string;
  isCorrect: boolean;
  llmAnalysis?: LLMAnalysis;
}

export interface LLMAnalysis {
  isCorrect: boolean;
  correctAnswers: string[];
  stepsCorrect: boolean;
  errors: {
    step: string;
    issue: string;
    correction: string;
  }[];
  feedback: string;
  strengths: string[];
  areasToImprove: string[];
}

export interface DiagnosticResult {
  totalQuestions: number;
  correctAnswers: number;
  skillsMastered: string[];
  skillsToImprove: string[];
  errors: ErrorAnalysis[];
}

export interface ErrorAnalysis {
  skill: string;
  errorType: string;
  description: string;
  recommendation: string;
  specificErrors?: {
    step: string;
    issue: string;
    correction: string;
  }[];
  strengths?: string[];
}

export interface Resource {
  type: 'video' | 'exercise' | 'lesson';
  title: string;
  description: string;
  url?: string;
  difficulty: 'easy' | 'medium' | 'hard';
}

export interface RemediationPlan {
  skills: string[];
  resources: Resource[];
}
