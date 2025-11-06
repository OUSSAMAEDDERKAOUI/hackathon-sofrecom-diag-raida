"""
Fallback Recommendations
Provides rule-based recommendations when LLM is unavailable
"""

from typing import Dict, Any, List


def generate_fallback_recommendations(
    student_data: Dict[str, Any],
    analysis_results: Dict[str, Any]
) -> str:
    """
    Generate rule-based recommendations as fallback
    
    Args:
        student_data: Student information
        analysis_results: Analysis results
        
    Returns:
        Formatted recommendations string
    """
    weak_areas = analysis_results.get('weak_areas', [])
    accuracy = analysis_results.get('accuracy', 0)
    difficulty_level = analysis_results.get('difficulty_level', 'intermediate')
    
    # Build recommendations
    recommendations = []
    
    # 1. Encouragement based on accuracy
    if accuracy >= 0.8:
        recommendations.append(
            "🎉 Excellent travail ! Tu maîtrises bien les concepts. "
            "Continue à pratiquer pour maintenir ce niveau."
        )
    elif accuracy >= 0.6:
        recommendations.append(
            "👍 Bon travail ! Tu es sur la bonne voie. "
            "Avec un peu plus de pratique, tu vas progresser rapidement."
        )
    elif accuracy >= 0.4:
        recommendations.append(
            "💪 Continue tes efforts ! Tu as compris certains concepts. "
            "Concentre-toi sur les domaines à améliorer."
        )
    else:
        recommendations.append(
            "🌟 Ne te décourage pas ! Les mathématiques demandent de la pratique. "
            "Commence par les bases et progresse étape par étape."
        )
    
    # 2. Specific recommendations for weak areas
    if weak_areas:
        recommendations.append("\n📚 Domaines à travailler:")
        
        for area in weak_areas[:3]:  # Top 3 weak areas
            area_recommendations = get_area_specific_recommendations(area)
            recommendations.append(f"\n• {area}:")
            recommendations.append(f"  {area_recommendations}")
    
    # 3. General study tips
    recommendations.append("\n💡 Conseils d'étude:")
    recommendations.extend(get_general_study_tips(difficulty_level))
    
    # 4. Next steps
    recommendations.append("\n🎯 Prochaines étapes:")
    recommendations.extend(get_next_steps(accuracy, weak_areas))
    
    return "\n".join(recommendations)


def get_area_specific_recommendations(area: str) -> str:
    """Get recommendations for specific math area"""
    
    area_tips = {
        'algebra': "Pratique la résolution d'équations simples avant de passer aux plus complexes. Utilise des exemples concrets.",
        'geometry': "Visualise les figures géométriques. Dessine des schémas pour mieux comprendre les propriétés.",
        'fractions': "Commence par les fractions simples. Utilise des objets du quotidien pour comprendre les parts.",
        'decimals': "Pratique les conversions entre fractions et décimaux. Utilise une calculatrice pour vérifier.",
        'equations': "Isole la variable étape par étape. Vérifie toujours ta solution en la substituant.",
        'word_problems': "Lis attentivement l'énoncé. Identifie les données et ce qui est demandé avant de calculer.",
        'percentages': "Relie les pourcentages aux fractions (50% = 1/2). Utilise des exemples de la vie quotidienne.",
        'ratios': "Comprends la relation entre les quantités. Utilise des tableaux pour organiser les données.",
        'statistics': "Pratique le calcul de moyennes avec des données simples. Crée des graphiques pour visualiser.",
        'probability': "Commence par des événements simples (pile ou face). Compte toutes les possibilités."
    }
    
    return area_tips.get(area.lower(), "Révise les concepts de base et pratique régulièrement avec des exercices variés.")


def get_general_study_tips(difficulty_level: str) -> List[str]:
    """Get general study tips based on difficulty level"""
    
    tips = [
        "• Pratique 15-20 minutes par jour plutôt qu'une longue session",
        "• Commence toujours par les exercices les plus faciles",
        "• N'hésite pas à demander de l'aide à ton professeur ou tes camarades",
        "• Utilise des ressources en ligne (vidéos, exercices interactifs)"
    ]
    
    if difficulty_level == 'beginner':
        tips.append("• Concentre-toi sur les bases avant d'avancer")
        tips.append("• Utilise des manipulations concrètes (objets, dessins)")
    elif difficulty_level == 'intermediate':
        tips.append("• Varie les types d'exercices pour renforcer ta compréhension")
        tips.append("• Essaie d'expliquer les concepts à quelqu'un d'autre")
    else:  # advanced
        tips.append("• Challenge-toi avec des problèmes plus complexes")
        tips.append("• Explore les applications réelles des mathématiques")
    
    return tips


def get_next_steps(accuracy: float, weak_areas: List[str]) -> List[str]:
    """Get recommended next steps"""
    
    steps = []
    
    if accuracy < 0.5:
        steps.append("1. Révise les concepts de base avec ton professeur")
        steps.append("2. Pratique des exercices simples pour gagner en confiance")
        steps.append("3. Identifie exactement ce que tu ne comprends pas")
    elif accuracy < 0.7:
        steps.append("1. Pratique régulièrement les domaines identifiés")
        steps.append("2. Fais des exercices progressifs (du plus simple au plus complexe)")
        steps.append("3. Vérifie ta compréhension avec des quiz")
    else:
        steps.append("1. Continue à pratiquer pour maintenir ton niveau")
        steps.append("2. Challenge-toi avec des exercices plus difficiles")
        steps.append("3. Aide tes camarades - enseigner renforce l'apprentissage")
    
    if weak_areas:
        steps.append(f"4. Focus sur: {', '.join(weak_areas[:2])}")
    
    return steps


def get_resource_suggestions(topic: str) -> List[str]:
    """Get resource suggestions for a topic"""
    
    resources = {
        'algebra': [
            "Khan Academy - Algèbre",
            "Exercices d'équations en ligne",
            "Vidéos explicatives sur les variables"
        ],
        'geometry': [
            "GeoGebra pour visualiser les figures",
            "Exercices de construction géométrique",
            "Vidéos sur les propriétés des formes"
        ],
        'fractions': [
            "Jeux interactifs sur les fractions",
            "Exercices de simplification",
            "Vidéos sur les opérations avec fractions"
        ]
    }
    
    return resources.get(topic.lower(), [
        "Ressources en ligne recommandées par ton professeur",
        "Exercices du manuel scolaire",
        "Vidéos éducatives sur YouTube"
    ])
