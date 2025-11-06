import { Question } from '../types';

export const equationQuestions: Question[] = [
  {
    id: 'q1',
    question: 'Résous l\'équation : 2x + 3 = 7',
    correctAnswer: '2',
    skill: 'Isolation de variable simple',
    context: 'Équation linéaire simple du premier degré'
  },
  {
    id: 'q2',
    question: 'Résous l\'équation : 3x - 5 = 10',
    correctAnswer: '5',
    skill: 'Isolation de variable avec soustraction',
    context: 'Équation linéaire avec terme négatif'
  },
  {
    id: 'q3',
    question: 'Résous l\'équation : -2x + 6 = 2',
    correctAnswer: '2',
    skill: 'Gestion des coefficients négatifs',
    context: 'Équation avec coefficient négatif devant x'
  },
  {
    id: 'q4',
    question: 'Résous l\'équation : 4(x + 2) = 20',
    correctAnswer: '3',
    skill: 'Distributivité et parenthèses',
    context: 'Équation nécessitant l\'application de la distributivité'
  },
  {
    id: 'q5',
    question: 'Résous l\'équation : (4x + 6)(3 - 7x) = 0',
    correctAnswer: '-3/2, 3/7',
    skill: 'Équations avec produit nul',
    context: 'Équation produit de facteurs - peut avoir plusieurs solutions'
  }
];
