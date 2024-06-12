"""
Module d'intégration numérique avec python de base

Ce module fournit plusieurs méthodes pour calculer l'intégrale d'un polynôme de degré 3 sur un intervalle donné [a, b].

Fonctions:
    - f: Calcule la valeur du polynôme de degré 3 à un point x donné.
    - analytique: Calcule l'intégrale analytique du polynôme de degré 3 sur [a, b].

Auteurs: Lou-Anne Villette & Thomas Chambeyron
Date: 05/06/2024
"""


# Fonction f(x)
def f(p, x):
    """
    Calcule la valeur du polynôme de degré 3 à un point x donné.

    Arguments:
    p (list) : liste des coefficients du polynôme
    x (float) : valeur à laquelle la fonction est évaluée

    Retour:
    (float) Valeur du polynôme f(x) = p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3
    """
    return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3


# Intégrale analytique
def analytique(p, a, b):
    """
    Calcule l'intégrale analytique du polynôme de degré 3 sur [a, b]

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration

    Retour:
    (float) Valeur de l'intégrale analytique de f(x) sur [a, b]
    """
    return (p[0] * (b - a) +
            p[1] * (b**2 - a**2) / 2 +
            p[2] * (b**3 - a**3) / 3 +
            p[3] * (b**4 - a**4) / 4)
