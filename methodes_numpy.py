"""
Module d'intégration numérique avec numpy

Ce module fournit plusieurs méthodes pour calculer l'intégrale d'un polynôme de degré 3 sur un intervalle donné [a, b].

Fonctions:
    - f: Calcule la valeur du polynôme de degré 3 à un point x donné.

Auteurs: Lou-Anne Villette & Thomas Chambeyron
Date: 05/06/2024
"""

import numpy as np


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
