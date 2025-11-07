import { useState } from 'react';
import { Welcome } from './components/Welcome';
import { Quiz } from './components/Quiz';
import { Results } from './components/Results';
import { RemediationPlanComponent } from './components/RemediationPlan';
import { Answer, ApiResponse, DiagnosticResult, RemediationPlan, RecommandationResource, RuleRaminder, Question } from './types';
import { analyzeAnswers, generateRemediationPlan } from './utils/analyzer';

type AppState = 'welcome' | 'quiz' | 'results' | 'plan';

export default function App() {
  const [appState, setAppState] = useState<AppState>('welcome');
  const [diagnostic, setDiagnostic] = useState<DiagnosticResult | null>(null);
  const [remediationPlan, setRemediationPlan] = useState<RemediationPlan | null>(null);
  const [answers, setAnswers] = useState<Answer[]>([]);
  const [ressources, setRessources] = useState<RecommandationResource[]>([])
  const [reminders, setReminders] = useState<RuleRaminder[]>([])

  const [questions, setQuestions] = useState<Question[]>([])
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleStartQuiz = () => {
    const callFlaskEndpoint = async () => {
        const url = 'http://127.0.0.1:5000/api/questions/';
  
        let req_body : any = {theme: 'first degree equations'}
  
        try {
            // Set initial state via props
            setError(null);
            setIsLoading(true);
  
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(req_body)
            });
  
            if (!response.ok) {
                const errorBody = await response.text();
                throw new Error(`HTTP error! Status: ${response.status}. Details: ${errorBody}`);
            }
  
            const data: ApiResponse = await response.json(); 
  
            let json_response = data.response.replace("```json\n", '')
            json_response = json_response.replace("\n```", '')
  
            let json : {questions: Question[]} = JSON.parse(json_response)
  
            console.log(json)
            
            setQuestions(json.questions)
            setAppState('quiz');
            
        } catch (err) {
            if (err instanceof Error) {
                console.error('Fetch error:', err.message);
                // 2. Update parent state with error
                setError(err.message);
            } else {
                setError("An unknown error occurred during fetch.");
            }
            
        } finally {
            // 3. Update parent loading state
            setIsLoading(false);
        }
    };
  
    callFlaskEndpoint()
  };

  const handleQuizComplete = async (userAnswers: Answer[]) => {
    const result = await analyzeAnswers(questions, userAnswers);
    const plan = generateRemediationPlan(result);
    
    setAnswers(userAnswers);
    setDiagnostic(result);
    setRemediationPlan(plan);
    setAppState('results');
  };

  const handleRecommandations = (res: RecommandationResource[]) => {
    setRessources(res)
  }
  const handleReminders = (reminder: RuleRaminder[]) => {
    setReminders(reminder)
  }

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

    if (isLoading == true) {
    return <span>Loading</span>
  }

  if (error !== null) {
    return <span>Error</span>
  }


  return (
    <div>
      {appState === 'welcome' && (
        <Welcome onStart={handleStartQuiz} />
      )}

      
      {appState === 'quiz' && (
        <Quiz 
          questions={questions}
          onComplete={handleQuizComplete}
        />
      )}
      
      {appState === 'results' && diagnostic && (
        <Results 
          diagnostic={diagnostic}
          questions={questions}
          answers={answers}
          onViewPlan={handleViewPlan}
          onRestart={handleRestart}
          onSetRecommandations={handleRecommandations}
          onSetReminders={handleReminders}
        />
      )}
      
      {appState === 'plan' && remediationPlan && (
        <RemediationPlanComponent 
          ressources={ressources}
          reminders={reminders}
          onBack={handleBackToResults}
          onRestart={handleRestart}
        />
      )}
    </div>
  );
}
