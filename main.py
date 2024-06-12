"""
Ce module exécute une série de comparaisons entre différentes méthodes d'intégration numérique pour une fonction
polynomiale de degré trois. Il affiche les résultats des méthodes, génère des graphiques de convergence et de temps
d'exécution, et compare les erreurs pour différents nombres de segments.

Fonctions:
    - main: Fonction principale du module qui exécute les comparaisons et génère les graphiques.

Auteur: Lou-Anne Villette & Thomas Chambeyron
Date: 11/06/2024
"""

import comparaisons


def main():
    """
    Fonction principale qui configure les paramètres d'intégration et exécute les comparaisons entre différentes
    méthodes d'intégration numérique. Elle affiche les résultats, et génère des graphiques de convergence, de temps
    d'exécution et des erreurs.
    """

    # Coefficients du polynôme et bornes de l'intervalle
    p = [1, 2, 3, 4]
    a, b = 0, 10

    # Liste des différents nombres de segments à utiliser pour les comparaisons
    segments = (list(range(10, 101, 10)) + list(range(200, 1001, 100))
                + list(range(2000, 10001, 1000)) + list(range(20000, 100001, 10000)))

    # Récupération des méthodes d'intégration à comparer
    methodes = comparaisons.methodes_a_comparer()

    # Affichage des résultats des différentes méthodes d'intégration
    comparaisons.resulat(p, a, b, methodes)

    # Génération et affichage des graphiques de convergence
    comparaisons.plot_convergence(p, a, b, segments, methodes)

    # Génération et affichage des graphiques de temps d'exécution
    comparaisons.plot_temps_execution(p, a, b, segments, methodes)

    # Génération et affichage des histogrammes des erreurs pour différents nombres de segments
    comparaisons.plot_erreur(p, a, b, [10, 100, 1000, 10000], methodes)


if __name__ == "__main__":
    main()
