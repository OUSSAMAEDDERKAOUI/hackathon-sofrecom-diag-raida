import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { RemediationPlan } from '../types';
import { Video, FileText, PenTool, ArrowLeft, ExternalLink } from 'lucide-react';

interface RemediationPlanProps {
  plan: RemediationPlan;
  onBack: () => void;
  onRestart: () => void;
}

export function RemediationPlanComponent({ plan, onBack, onRestart }: RemediationPlanProps) {
  const getResourceIcon = (type: string) => {
    switch (type) {
      case 'video': return <Video className="w-5 h-5" />;
      case 'exercise': return <PenTool className="w-5 h-5" />;
      case 'lesson': return <FileText className="w-5 h-5" />;
      default: return <FileText className="w-5 h-5" />;
    }
  };

  const getResourceColor = (type: string) => {
    switch (type) {
      case 'video': return 'border-red-200 bg-red-50';
      case 'exercise': return 'border-blue-200 bg-blue-50';
      case 'lesson': return 'border-green-200 bg-green-50';
      default: return 'border-gray-200 bg-gray-50';
    }
  };

  const getDifficultyBadge = (difficulty: string) => {
    const colors = {
      easy: 'bg-green-500',
      medium: 'bg-yellow-500',
      hard: 'bg-red-500'
    };
    const labels = {
      easy: 'Facile',
      medium: 'Moyen',
      hard: 'Difficile'
    };
    return (
      <Badge className={`${colors[difficulty as keyof typeof colors]} text-white`}>
        {labels[difficulty as keyof typeof labels]}
      </Badge>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6">
      <div className="max-w-4xl mx-auto pt-8">
        <Button 
          onClick={onBack}
          variant="ghost"
          className="mb-6"
        >
          <ArrowLeft className="mr-2 w-4 h-4" />
          Retour aux résultats
        </Button>

        <div className="text-center mb-8">
          <h2 className="mb-2">Votre plan de soutien personnalisé</h2>
          <p className="text-gray-600">
            Ressources sélectionnées pour renforcer vos compétences
          </p>
        </div>

        {plan.skills.length > 0 && (
          <Card className="border-2 border-purple-200 mb-6">
            <CardHeader>
              <CardTitle className="text-purple-700">Compétences à travailler</CardTitle>
              <CardDescription>
                Voici les domaines sur lesquels vous concentrer
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2">
                {plan.skills.map((skill, index) => (
                  <Badge key={index} variant="outline" className="text-purple-700 border-purple-300">
                    {skill}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        <div className="mb-6">
          <h3 className="mb-4">Ressources recommandées</h3>
          
          {plan.resources.length > 0 ? (
            <div className="space-y-4">
              {plan.resources.map((resource, index) => (
                <Card key={index} className={`border-2 ${getResourceColor(resource.type)} hover:shadow-lg transition-shadow`}>
                  <CardHeader>
                    <div className="flex items-start justify-between">
                      <div className="flex items-start gap-3 flex-1">
                        <div className={`p-2 rounded-lg ${
                          resource.type === 'video' ? 'bg-red-100 text-red-600' :
                          resource.type === 'exercise' ? 'bg-blue-100 text-blue-600' :
                          'bg-green-100 text-green-600'
                        }`}>
                          {getResourceIcon(resource.type)}
                        </div>
                        <div className="flex-1">
                          <CardTitle className="text-lg mb-1">{resource.title}</CardTitle>
                          <CardDescription>{resource.description}</CardDescription>
                        </div>
                      </div>
                      <div>
                        {getDifficultyBadge(resource.difficulty)}
                      </div>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <Button 
                      variant="outline" 
                      className="w-full"
                      onClick={() => window.open(resource.url, '_blank')}
                    >
                      Accéder à la ressource
                      <ExternalLink className="ml-2 w-4 h-4" />
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          ) : (
            <Card>
              <CardContent className="pt-6">
                <p className="text-center text-gray-600">
                  Félicitations ! Vous avez maîtrisé toutes les compétences évaluées.
                </p>
              </CardContent>
            </Card>
          )}
        </div>

        <Card className="border-2 border-blue-200 bg-gradient-to-r from-blue-50 to-purple-50 mb-6">
          <CardHeader>
            <CardTitle className="text-blue-700">Conseils pour progresser</CardTitle>
          </CardHeader>
          <CardContent className="space-y-2 text-gray-700">
            <p className="flex items-start">
              <span className="text-blue-600 mr-2">1.</span>
              Commencez par les ressources marquées "Facile" avant de passer aux niveaux supérieurs
            </p>
            <p className="flex items-start">
              <span className="text-blue-600 mr-2">2.</span>
              Regardez les vidéos en premier pour comprendre les concepts
            </p>
            <p className="flex items-start">
              <span className="text-blue-600 mr-2">3.</span>
              Pratiquez régulièrement avec les exercices proposés
            </p>
            <p className="flex items-start">
              <span className="text-blue-600 mr-2">4.</span>
              N'hésitez pas à refaire le diagnostic après avoir travaillé ces ressources
            </p>
          </CardContent>
        </Card>

        <div className="flex gap-4">
          <Button 
            onClick={onRestart}
            className="flex-1 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
            size="lg"
          >
            Refaire le diagnostic
          </Button>
        </div>

        <div className="text-center mt-8 text-sm text-gray-500">
          <p>Initiative Madrasa Raida • Alignée sur l'ODD n°4 UNESCO</p>
        </div>
      </div>
    </div>
  );
}
