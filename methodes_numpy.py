"""
Module d'intégration numérique avec numpy

Ce module fournit plusieurs méthodes pour calculer l'intégrale d'un polynôme de degré 3 sur un intervalle donné [a, b].

Fonctions:
    - f: Calcule la valeur du polynôme de degré 3 à un point x donné.
    - rectangles: Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec la méthode des rectangles vectorisée.

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


# Méthode des rectangles
def rectangles(p, a, b, n=10):
    """
    Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec la méthode des rectangles vectorisée.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)

    Retour:
    (float) Valeur approximative de l'intégrale de f(x) sur [a, b] par la méthode des rectangles vectorisée
    """
    pas = (b - a) / n
    x = np.linspace(a, b, n, endpoint=False)
    return np.sum(f(p, x + 0.5 * pas) * pas)
