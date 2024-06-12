"""
Ce module exécute une série de comparaisons entre différentes méthodes d'intégration numérique pour une fonction
polynomiale de degré trois. Il affiche les résultats des méthodes, génère des graphiques de convergence et de temps
d'exécution, et compare les erreurs pour différents nombres de segments.

Fonctions:
    - main: Fonction principale du module qui exécute les comparaisons et génère les graphiques.

Auteur: Lou-Anne Villette & Thomas Chambeyron
Date: 05/06/2024
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


if __name__ == "__main__":
    main()
