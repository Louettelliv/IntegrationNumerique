"""
Module de comparaison des méthodes d'intégration numériques

Ce module permet de comparer différentes méthodes d'intégration numérique pour un polynôme de degré 3.
Les méthodes de comparaison incluent le calcul de l'erreur, l'analyse de la convergence, et la mesure du temps
d'exécution.

Fonctions:
    - erreur_absolue: Calcule l'erreur absolue entre l'intégrale analytique et l'intégrale numérique.
    - erreur_integration: Retourne l'erreur absolue pour un nombre donné de segments.
    - temps_execution: Mesure le temps d'exécution d'une méthode d'intégration.

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


# Fonction pour retourner l'erreur pour un nombre de segments
def erreur_integration(p, a, b, methode, n=10):
    """
    Retourne l'erreur pour un nombre donné de segments.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)
    methode (fct) : méthode d'intégration utilisée

    Retour:
    (float) Erreur absolue d'intégration pour la méthode et le nombre de segments donnés
    """
    analytique = methodes_python.analytique(p, a, b)
    numerique = methode(p, a, b, n)
    return erreur_absolue(analytique, numerique)


# Fonction pour mesurer le temps d'exécution
def temps_execution(methode, p, a, b, n=10):
    """
    Mesure le temps d'exécution d'une méthode d'intégration.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)
    methode (fct) : méthode d'intégration utilisée

    Retour:
    (float) Temps d'exécution moyen en secondes de la méthode pour les paramètres donnés
    """
    return timeit(lambda: methode(p, a, b, n), number=10)/10
