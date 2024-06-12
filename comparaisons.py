"""
Module de comparaison des méthodes d'intégration numériques

Ce module permet de comparer différentes méthodes d'intégration numérique pour un polynôme de degré 3.
Les méthodes de comparaison incluent le calcul de l'erreur, l'analyse de la convergence, et la mesure du temps
d'exécution.

Fonctions:
    - erreur_absolue: Calcule l'erreur absolue entre l'intégrale analytique et l'intégrale numérique.

Auteurs: Lou-Anne Villette & Thomas Chambeyron
Date: 05/06/2024
"""

import methodes_python
import methodes_numpy
import methodes_scipy

from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np


# Calcul de l'erreur
def erreur_absolue(analytique, numerique):
    """
    Calcule l'erreur absolue entre l'intégrale analytique et l'intégrale numérique.

    Arguments:
    analytique (float) : valeur de l'intégrale analytique
    numerique (float) : valeur de l'intégrale numérique

    Retour:
    (float) Erreur absolue entre les deux valeurs
    """
    return abs(analytique - numerique)
