import { useState } from 'react';
import { Welcome } from './components/Welcome';
import { Quiz } from './components/Quiz';
import { Results } from './components/Results';
import { RemediationPlanComponent } from './components/RemediationPlan';
import { equationQuestions } from './data/questions';
import { Answer, DiagnosticResult, RemediationPlan } from './types';
import { analyzeAnswers, generateRemediationPlan } from './utils/analyzer';

type AppState = 'welcome' | 'quiz' | 'results' | 'plan';

export default function App() {
  const [appState, setAppState] = useState<AppState>('welcome');
  const [diagnostic, setDiagnostic] = useState<DiagnosticResult | null>(null);
  const [remediationPlan, setRemediationPlan] = useState<RemediationPlan | null>(null);
  const [answers, setAnswers] = useState<Answer[]>([]);

  const handleStartQuiz = () => {
    setAppState('quiz');
  };

  const handleQuizComplete = async (userAnswers: Answer[]) => {
    const result = await analyzeAnswers(equationQuestions, userAnswers);
    const plan = generateRemediationPlan(result);
    
    setAnswers(userAnswers);
    setDiagnostic(result);
    setRemediationPlan(plan);
    setAppState('results');
  };

  const handleViewPlan = () => {
    setAppState('plan');
  };

  const handleBackToResults = () => {
    setAppState('results');
  };

  const handleRestart = () => {
    setDiagnostic(null);
    setRemediationPlan(null);
    setAnswers([]);
    setAppState('welcome');
  };

  return (
    <div>
      {appState === 'welcome' && (
        <Welcome onStart={handleStartQuiz} />
      )}
      
      {appState === 'quiz' && (
        <Quiz 
          questions={equationQuestions}
          onComplete={handleQuizComplete}
        />
      )}
      
      {appState === 'results' && diagnostic && (
        <Results 
          diagnostic={diagnostic}
          questions={equationQuestions}
          answers={answers}
          onViewPlan={handleViewPlan}
          onRestart={handleRestart}
        />
      )}
      
      {appState === 'plan' && remediationPlan && (
        <RemediationPlanComponent 
          plan={remediationPlan}
          onBack={handleBackToResults}
          onRestart={handleRestart}
        />
      )}
    </div>
  );
}
