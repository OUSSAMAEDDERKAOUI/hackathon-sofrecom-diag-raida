import { useState } from 'react';
import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Textarea } from "./ui/textarea";
import { Progress } from "./ui/progress";
import { Question, Answer, ApiResponse } from '../types';
import { ChevronRight, AlertCircle, Lightbulb, Loader2 } from 'lucide-react';
import { Alert, AlertDescription } from "./ui/alert";
import { analyzeSolutionWithLLM } from '../utils/llm-analyzer';
import exampleImage from 'figma:asset/5c7e91272cb3bf18525dd31fdf255f6af0778d09.png';

interface QuizProps {
  questions: Question[],
  onComplete: (answers: Answer[]) => void;
}

export function Quiz({ questions, onComplete }: QuizProps) {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<Answer[]>([]);
  const [solutionText, setSolutionText] = useState('');
  const [showError, setShowError] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const currentQuestion = questions[currentQuestionIndex];
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100;

  const handleNext = async () => {
    if (!solutionText.trim()) {
      setShowError(true);
      return;
    }

    setShowError(false);
    setIsAnalyzing(true);

    try {
      // Analyze solution with LLM
      const llmAnalysis = await analyzeSolutionWithLLM(currentQuestion, solutionText);

      const answer: Answer = {
        questionId: currentQuestion.id,
        solutionText: solutionText.trim(),
        isCorrect: llmAnalysis.isCorrect,
        llmAnalysis
      };

      const newAnswers = [...answers, answer];
      setAnswers(newAnswers);
      setSolutionText('');
      setShowHint(false);
      setIsAnalyzing(false);

      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
      } else {
        onComplete(newAnswers);
      }
    } catch (error) {
      console.error('Error analyzing solution:', error);
      setIsAnalyzing(false);
      // Continue anyway with basic analysis
      const answer: Answer = {
        questionId: currentQuestion.id,
        solutionText: solutionText.trim(),
        isCorrect: false,
      };
      const newAnswers = [...answers, answer];
      setAnswers(newAnswers);
      setSolutionText('');
      
      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
      } else {
        onComplete(newAnswers);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6">
      <div className="max-w-4xl mx-auto pt-8">
        <div className="mb-8">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-gray-600">
              Question {currentQuestionIndex + 1} sur {questions.length}
            </span>
            <span className="text-sm text-gray-600">
              {Math.round(progress)}% complété
            </span>
          </div>
          <Progress value={progress} className="h-2" />
        </div>

        <Card className="border-2 border-blue-200 mb-6">
          <CardHeader>
            <CardTitle>Question {currentQuestionIndex + 1}</CardTitle>
            <CardDescription className="text-blue-600">
              Compétence évaluée : {currentQuestion.skill}
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-lg border border-blue-100">
              <p className="text-center text-xl text-gray-800">
                {currentQuestion.question}
              </p>
            </div>

            <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
              <p className="text-sm text-gray-700 mb-2">
                <strong>Instructions :</strong> Écrivez votre solution complète comme vous le feriez sur papier.
                Montrez toutes vos étapes de raisonnement, vos calculs et votre réponse finale.
              </p>
              <Button
                variant="ghost"
                size="sm"
                onClick={() => setShowHint(!showHint)}
                className="text-blue-600"
              >
                <Lightbulb className="w-4 h-4 mr-2" />
                {showHint ? 'Masquer l\'exemple' : 'Voir un exemple'}
              </Button>
            </div>

            {showHint && (
              <div className="bg-purple-50 p-4 rounded-lg border border-purple-200 space-y-3">
                <p className="text-sm text-purple-900">
                  <strong>Exemple de solution bien rédigée :</strong>
                </p>
                <div className="bg-white p-3 rounded border border-purple-200">
                  <img 
                    src={exampleImage} 
                    alt="Exemple de solution mathématique" 
                    className="w-full max-w-md mx-auto"
                  />
                </div>
                <div className="text-sm text-purple-800 space-y-1">
                  <p>✓ Écrivez vos équations clairement</p>
                  <p>✓ Montrez chaque étape de calcul</p>
                  <p>✓ Indiquez votre raisonnement (ex: "Soit :", "Donc :", "Or")</p>
                  <p>✓ Pour une équation produit, trouvez toutes les solutions</p>
                  <p>✓ Donnez votre réponse finale clairement</p>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        <Card className="border-2 border-purple-200 mb-6">
          <CardHeader>
            <CardTitle>Votre solution</CardTitle>
            <CardDescription>
              Écrivez ici comme vous le feriez sur une feuille
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <Textarea
              value={solutionText}
              onChange={(e) => setSolutionText(e.target.value)}
              placeholder="Exemple :
Équation : 2x + 3 = 7

Soit : 2x + 3 = 7
       2x = 7 - 3
       2x = 4
       x = 4/2
       x = 2

Donc x = 2"
              className="min-h-[300px] font-mono text-base"
              disabled={isAnalyzing}
            />

            <div className="text-xs text-gray-500 space-y-1">
              <p>💡 Conseils :</p>
              <p>• Utilisez "x" pour la variable</p>
              <p>• Écrivez les fractions avec "/" (ex: 3/2)</p>
              <p>• Pour plusieurs solutions, utilisez "ou" ou "et"</p>
              <p>• Montrez clairement votre réponse finale</p>
            </div>

            {showError && (
              <Alert variant="destructive">
                <AlertCircle className="h-4 w-4" />
                <AlertDescription>
                  Veuillez écrire votre solution avant de continuer.
                </AlertDescription>
              </Alert>
            )}

            <Button 
              onClick={handleNext}
              disabled={isAnalyzing}
              className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
              size="lg"
            >
              {isAnalyzing ? (
                <>
                  <Loader2 className="mr-2 w-5 h-5 animate-spin" />
                  Analyse en cours...
                </>
              ) : currentQuestionIndex < questions.length - 1 ? (
                <>
                  Question suivante <ChevronRight className="ml-2 w-5 h-5" />
                </>
              ) : (
                'Terminer le diagnostic'
              )}
            </Button>
          </CardContent>
        </Card>

        <div className="text-center text-sm text-gray-500">
          <p>L'IA analysera votre raisonnement et vos calculs pour vous donner un retour personnalisé.</p>
        </div>
      </div>
    </div>
  );
}
