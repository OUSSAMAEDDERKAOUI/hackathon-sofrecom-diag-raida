import { Resource } from '../types';

export const resourceDatabase: { [skill: string]: Resource[] } = {
  'Isolation de variable simple': [
    {
      type: 'video',
      title: 'Isoler la variable dans une équation simple',
      description: 'Apprendre à isoler x en utilisant les opérations inverses',
      url: '#',
      difficulty: 'easy'
    },
    {
      type: 'exercise',
      title: 'Exercices d\'isolation de base',
      description: '10 équations simples du type ax + b = c',
      url: '#',
      difficulty: 'easy'
    },
    {
      type: 'lesson',
      title: 'Les opérations inverses',
      description: 'Comprendre comment annuler une opération',
      url: '#',
      difficulty: 'easy'
    }
  ],
  'Isolation de variable avec soustraction': [
    {
      type: 'video',
      title: 'Gérer les soustractions dans les équations',
      description: 'Technique pour déplacer les termes soustractifs',
      url: '#',
      difficulty: 'easy'
    },
    {
      type: 'exercise',
      title: 'Pratique : équations avec soustraction',
      description: 'Exercices progressifs avec termes négatifs',
      url: '#',
      difficulty: 'medium'
    }
  ],
  'Gestion des coefficients négatifs': [
    {
      type: 'video',
      title: 'Les nombres négatifs dans les équations',
      description: 'Comment gérer un coefficient négatif devant x',
      url: '#',
      difficulty: 'medium'
    },
    {
      type: 'lesson',
      title: 'Règles des signes',
      description: 'Révision complète des règles avec les nombres négatifs',
      url: '#',
      difficulty: 'easy'
    },
    {
      type: 'exercise',
      title: 'Exercices avec coefficients négatifs',
      description: 'Entraînement ciblé sur les signes',
      url: '#',
      difficulty: 'medium'
    }
  ],
  'Distributivité et parenthèses': [
    {
      type: 'video',
      title: 'La propriété distributive',
      description: 'Comprendre et appliquer a(b + c) = ab + ac',
      url: '#',
      difficulty: 'medium'
    },
    {
      type: 'lesson',
      title: 'Développer avant de résoudre',
      description: 'Méthodologie pour les équations avec parenthèses',
      url: '#',
      difficulty: 'medium'
    },
    {
      type: 'exercise',
      title: 'Équations avec parenthèses',
      description: 'Pratique de la distributivité et résolution',
      url: '#',
      difficulty: 'medium'
    }
  ],
  'Équations avec variable des deux côtés': [
    {
      type: 'video',
      title: 'Regrouper les termes en x',
      description: 'Technique pour résoudre quand x apparaît des deux côtés',
      url: '#',
      difficulty: 'hard'
    },
    {
      type: 'lesson',
      title: 'Méthodologie complète',
      description: 'Stratégie étape par étape pour ce type d\'équation',
      url: '#',
      difficulty: 'medium'
    },
    {
      type: 'exercise',
      title: 'Entraînement avancé',
      description: 'Équations complexes avec x des deux côtés',
      url: '#',
      difficulty: 'hard'
    }
  ]
};
