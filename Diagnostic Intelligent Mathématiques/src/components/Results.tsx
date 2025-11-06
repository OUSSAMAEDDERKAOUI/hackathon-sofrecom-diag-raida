import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { Separator } from "./ui/separator";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { DiagnosticResult, Question, Answer } from '../types';
import { CheckCircle, XCircle, AlertTriangle, BookOpen, FileText } from 'lucide-react';

interface ResultsProps {
  diagnostic: DiagnosticResult;
  questions: Question[];
  answers: Answer[];
  onViewPlan: () => void;
  onRestart: () => void;
}

export function Results({ diagnostic, questions, answers, onViewPlan, onRestart }: ResultsProps) {
  const percentage = Math.round((diagnostic.correctAnswers / diagnostic.totalQuestions) * 100);
  
  const getPerformanceLevel = (percent: number) => {
    if (percent >= 80) return { label: 'Excellent', color: 'bg-green-500', textColor: 'text-green-700' };
    if (percent >= 60) return { label: 'Bon', color: 'bg-blue-500', textColor: 'text-blue-700' };
    if (percent >= 40) return { label: 'Moyen', color: 'bg-yellow-500', textColor: 'text-yellow-700' };
    return { label: 'À améliorer', color: 'bg-red-500', textColor: 'text-red-700' };
  };

  const performance = getPerformanceLevel(percentage);

  // Separate correct and incorrect answers
  const correctAnswers = answers.filter(a => a.isCorrect);
  const incorrectAnswers = answers.filter(a => !a.isCorrect);
  
  const getQuestionForAnswer = (answer: Answer) => {
    return questions.find(q => q.id === answer.questionId);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6">
      <div className="max-w-4xl mx-auto pt-8">
        <div className="text-center mb-8">
          <div className="flex justify-center mb-4">
            <div className="w-24 h-24 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
              <FileText className="w-12 h-12 text-white" />
            </div>
          </div>
          <h2 className="mb-2">Résultats du diagnostic</h2>
          <p className="text-gray-600">
            Analyse personnalisée de vos compétences
          </p>
        </div>

        <Card className="border-2 border-blue-200 mb-6">
          <CardHeader className="text-center">
            <div className="flex justify-center mb-4">
              <div className="relative">
                <div className="w-32 h-32 rounded-full border-8 border-gray-200 flex items-center justify-center">
                  <div className={`absolute inset-0 rounded-full border-8 ${performance.color} border-t-transparent border-l-transparent transform -rotate-45`} 
                       style={{ clipPath: `polygon(50% 50%, 50% 0%, ${50 + percentage/2}% 0%, ${50 + percentage/2}% 100%, 50% 100%)` }}>
                  </div>
                  <div className="text-4xl z-10">{percentage}%</div>
                </div>
              </div>
            </div>
            <CardTitle>
              {diagnostic.correctAnswers} / {diagnostic.totalQuestions} réponses correctes
            </CardTitle>
            <CardDescription>
              <Badge className={`${performance.color} text-white mt-2`}>
                {performance.label}
              </Badge>
            </CardDescription>
          </CardHeader>
        </Card>

        <div className="grid md:grid-cols-2 gap-6 mb-6">
          <Card className="border-2 border-green-200 bg-green-50">
            <CardHeader>
              <div className="flex items-center gap-2">
                <CheckCircle className="w-6 h-6 text-green-600" />
                <CardTitle className="text-green-700">Compétences maîtrisées</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              {diagnostic.skillsMastered.length > 0 ? (
                <ul className="space-y-2">
                  {diagnostic.skillsMastered.map((skill, index) => (
                    <li key={index} className="flex items-start">
                      <CheckCircle className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                      <span className="text-green-800">{skill}</span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-green-700">
                  Aucune compétence entièrement maîtrisée pour le moment.
                </p>
              )}
            </CardContent>
          </Card>

          <Card className="border-2 border-orange-200 bg-orange-50">
            <CardHeader>
              <div className="flex items-center gap-2">
                <AlertTriangle className="w-6 h-6 text-orange-600" />
                <CardTitle className="text-orange-700">Points à renforcer</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              {diagnostic.skillsToImprove.length > 0 ? (
                <ul className="space-y-2">
                  {diagnostic.skillsToImprove.map((skill, index) => (
                    <li key={index} className="flex items-start">
                      <AlertTriangle className="w-5 h-5 text-orange-600 mr-2 mt-0.5 flex-shrink-0" />
                      <span className="text-orange-800">{skill}</span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-orange-700">
                  Excellent ! Toutes les compétences sont maîtrisées.
                </p>
              )}
            </CardContent>
          </Card>
        </div>

        <Tabs defaultValue="incorrect" className="mb-6">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="incorrect" className="flex items-center gap-2">
              <XCircle className="w-4 h-4" />
              Questions à revoir ({incorrectAnswers.length})
            </TabsTrigger>
            <TabsTrigger value="correct" className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4" />
              Questions réussies ({correctAnswers.length})
            </TabsTrigger>
          </TabsList>

          <TabsContent value="incorrect" className="mt-4">
            {diagnostic.errors.length > 0 ? (
              <Card className="border-2 border-red-200">
                <CardHeader>
                  <div className="flex items-center gap-2">
                    <XCircle className="w-6 h-6 text-red-600" />
                    <CardTitle className="text-red-700">Analyse détaillée par l'IA</CardTitle>
                  </div>
                  <CardDescription>
                    Analyse intelligente de votre raisonnement et de vos calculs
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  {incorrectAnswers.map((answer, index) => {
                    const question = getQuestionForAnswer(answer);
                    const error = diagnostic.errors[index];
                    if (!question || !error) return null;
                    
                    return (
                      <div key={answer.questionId}>
                        {index > 0 && <Separator className="my-4" />}
                        <div className="space-y-3">
                          <div className="bg-gray-50 p-3 rounded-lg border border-gray-200">
                            <div className="flex items-start gap-2 mb-2">
                              <Badge variant="outline" className="text-red-600 border-red-300">
                                Question {questions.findIndex(q => q.id === answer.questionId) + 1}
                              </Badge>
                              <span className="text-sm text-gray-600">{error.skill}</span>
                            </div>
                            <p className="text-gray-800 mb-2">
                              <strong>Question :</strong> {question.question}
                            </p>
                            <div className="bg-white p-2 rounded border border-gray-300">
                              <p className="text-xs text-gray-600 mb-1"><strong>Votre solution :</strong></p>
                              <pre className="text-sm whitespace-pre-wrap font-mono text-gray-700">{answer.solutionText}</pre>
                            </div>
                          </div>

                          {error.strengths && error.strengths.length > 0 && (
                            <div className="bg-green-50 p-3 rounded-lg border border-green-200">
                              <p className="text-sm text-green-800 mb-2">
                                <strong>✓ Points forts :</strong>
                              </p>
                              <ul className="space-y-1">
                                {error.strengths.map((strength, i) => (
                                  <li key={i} className="text-sm text-green-700 flex items-start">
                                    <CheckCircle className="w-4 h-4 mr-2 mt-0.5 flex-shrink-0" />
                                    {strength}
                                  </li>
                                ))}
                              </ul>
                            </div>
                          )}
                          
                          <div className="bg-red-50 p-3 rounded-lg border border-red-200">
                            <p className="text-sm text-red-800 mb-1">
                              <strong>Type d'erreur :</strong> {error.errorType}
                            </p>
                            <p className="text-sm text-red-700 mb-3">
                              {error.description}
                            </p>
                            
                            {error.specificErrors && error.specificErrors.length > 0 && (
                              <div className="space-y-2 mb-3">
                                <p className="text-sm text-red-800">
                                  <strong>Erreurs détectées :</strong>
                                </p>
                                {error.specificErrors.map((specificError, i) => (
                                  <div key={i} className="bg-white p-2 rounded border border-red-300">
                                    <p className="text-xs text-gray-600 mb-1">
                                      <strong>Étape :</strong> <code>{specificError.step}</code>
                                    </p>
                                    <p className="text-xs text-red-700 mb-1">
                                      <strong>Problème :</strong> {specificError.issue}
                                    </p>
                                    <p className="text-xs text-green-700">
                                      <strong>Correction :</strong> {specificError.correction}
                                    </p>
                                  </div>
                                ))}
                              </div>
                            )}
                            
                            <div className="bg-white p-2 rounded border border-red-200">
                              <p className="text-sm text-gray-700">
                                <strong>💡 Recommandation :</strong> {error.recommendation}
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </CardContent>
              </Card>
            ) : (
              <Card className="border-2 border-green-200 bg-green-50">
                <CardContent className="pt-6">
                  <div className="text-center text-green-700">
                    <CheckCircle className="w-16 h-16 mx-auto mb-4 text-green-600" />
                    <p className="text-lg">Parfait ! Toutes les réponses sont correctes.</p>
                  </div>
                </CardContent>
              </Card>
            )}
          </TabsContent>

          <TabsContent value="correct" className="mt-4">
            {correctAnswers.length > 0 ? (
              <Card className="border-2 border-green-200 bg-green-50">
                <CardHeader>
                  <div className="flex items-center gap-2">
                    <CheckCircle className="w-6 h-6 text-green-600" />
                    <CardTitle className="text-green-700">Questions réussies</CardTitle>
                  </div>
                  <CardDescription className="text-green-800">
                    Bravo ! Voici les questions que vous avez correctement résolues
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  {correctAnswers.map((answer, index) => {
                    const question = getQuestionForAnswer(answer);
                    if (!question) return null;
                    
                    return (
                      <div key={answer.questionId}>
                        {index > 0 && <Separator className="my-4" />}
                        <div className="bg-white p-4 rounded-lg border border-green-300 space-y-3">
                          <div className="flex items-start gap-2">
                            <Badge className="bg-green-600 text-white">
                              Question {questions.findIndex(q => q.id === answer.questionId) + 1}
                            </Badge>
                            <span className="text-sm text-green-700">{question.skill}</span>
                          </div>
                          
                          <div className="space-y-2">
                            <p className="text-gray-800">
                              <strong>Question :</strong> {question.question}
                            </p>
                            
                            <div className="bg-green-50 p-3 rounded border border-green-200">
                              <p className="text-xs text-green-700 mb-2">
                                <strong>Votre solution :</strong>
                              </p>
                              <pre className="text-sm whitespace-pre-wrap font-mono text-gray-700">{answer.solutionText}</pre>
                            </div>

                            {answer.llmAnalysis?.strengths && answer.llmAnalysis.strengths.length > 0 && (
                              <div className="bg-green-100 p-2 rounded border border-green-300">
                                <p className="text-xs text-green-800 mb-1">
                                  <strong>✓ Points forts :</strong>
                                </p>
                                <ul className="space-y-1">
                                  {answer.llmAnalysis.strengths.map((strength, i) => (
                                    <li key={i} className="text-xs text-green-700 flex items-start">
                                      <CheckCircle className="w-3 h-3 mr-1 mt-0.5 flex-shrink-0" />
                                      {strength}
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}
                            
                            <div className="flex items-center gap-2 text-green-700">
                              <CheckCircle className="w-5 h-5" />
                              <span className="text-sm">Réponse correcte : {question.correctAnswer}</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </CardContent>
              </Card>
            ) : (
              <Card className="border-2 border-orange-200 bg-orange-50">
                <CardContent className="pt-6">
                  <div className="text-center text-orange-700">
                    <AlertTriangle className="w-16 h-16 mx-auto mb-4 text-orange-600" />
                    <p className="text-lg">Aucune question n'a été réussie.</p>
                    <p className="text-sm mt-2">Consultez le plan de soutien pour progresser !</p>
                  </div>
                </CardContent>
              </Card>
            )}
          </TabsContent>
        </Tabs>

        <div className="flex gap-4">
          <Button 
            onClick={onViewPlan}
            className="flex-1 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            size="lg"
          >
            <BookOpen className="mr-2 w-5 h-5" />
            Voir mon plan de soutien
          </Button>
          <Button 
            onClick={onRestart}
            variant="outline"
            size="lg"
          >
            Recommencer
          </Button>
        </div>
      </div>
    </div>
  );
}
