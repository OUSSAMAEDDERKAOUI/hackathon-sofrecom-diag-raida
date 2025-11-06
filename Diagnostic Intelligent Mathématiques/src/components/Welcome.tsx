import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Target, TrendingUp, BookOpen } from "lucide-react";

interface WelcomeProps {
  onStart: () => void;
}

export function Welcome({ onStart }: WelcomeProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12 pt-12">
          <div className="flex justify-center mb-6">
            <div className="w-20 h-20 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
              <Target className="w-10 h-10 text-white" />
            </div>
          </div>
          <h1 className="mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            Diag-Raida
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            Diagnostiquer, Comprendre, Réapprendre
          </p>
          <p className="text-gray-500">
            Une boussole intelligente pour guider chaque élève vers la réussite 🎯
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-12">
          <Card>
            <CardHeader>
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                <Target className="w-6 h-6 text-blue-600" />
              </div>
              <CardTitle>Diagnostiquer</CardTitle>
              <CardDescription>
                Évaluez vos compétences réelles en mathématiques avec un quiz adaptatif
              </CardDescription>
            </CardHeader>
          </Card>

          <Card>
            <CardHeader>
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                <TrendingUp className="w-6 h-6 text-purple-600" />
              </div>
              <CardTitle>Comprendre</CardTitle>
              <CardDescription>
                Identifiez précisément vos lacunes et les types d'erreurs commises
              </CardDescription>
            </CardHeader>
          </Card>

          <Card>
            <CardHeader>
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                <BookOpen className="w-6 h-6 text-green-600" />
              </div>
              <CardTitle>Réapprendre</CardTitle>
              <CardDescription>
                Recevez un plan personnalisé avec exercices et ressources adaptés
              </CardDescription>
            </CardHeader>
          </Card>
        </div>

        <Card className="border-2 border-blue-200 bg-gradient-to-br from-blue-50 to-purple-50">
          <CardHeader>
            <CardTitle>Thème du diagnostic</CardTitle>
            <CardDescription>
              Résolution d'équations du premier degré
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <p className="text-gray-700 mb-2">
                  Ce diagnostic évalue votre maîtrise des compétences suivantes :
                </p>
                <ul className="space-y-2 text-gray-600">
                  <li className="flex items-start">
                    <span className="text-blue-600 mr-2">•</span>
                    Isolation de variable simple
                  </li>
                  <li className="flex items-start">
                    <span className="text-blue-600 mr-2">•</span>
                    Gestion des coefficients négatifs
                  </li>
                  <li className="flex items-start">
                    <span className="text-blue-600 mr-2">•</span>
                    Distributivité et parenthèses
                  </li>
                  <li className="flex items-start">
                    <span className="text-blue-600 mr-2">•</span>
                    Équations avec variables des deux côtés
                  </li>
                </ul>
              </div>
              
              <div className="bg-white rounded-lg p-4 border border-blue-200">
                <p className="text-sm text-gray-600">
                  <strong>Durée estimée :</strong> 10-15 minutes<br />
                  <strong>Nombre de questions :</strong> 5<br />
                  <strong>Format :</strong> Questions ouvertes
                </p>
              </div>

              <Button 
                onClick={onStart}
                className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
                size="lg"
              >
                Commencer le diagnostic
              </Button>
            </div>
          </CardContent>
        </Card>

        <div className="text-center mt-8 text-sm text-gray-500">
          <p>Initiative Madrasa Raida • Alignée sur l'ODD n°4 UNESCO</p>
        </div>
      </div>
    </div>
  );
}
