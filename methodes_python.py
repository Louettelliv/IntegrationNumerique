"""
Module d'intégration numérique avec python de base

Ce module fournit plusieurs méthodes pour calculer l'intégrale d'un polynôme de degré 3 sur un intervalle donné [a, b].

Fonctions:
    - f: Calcule la valeur du polynôme de degré 3 à un point x donné.
    - analytique: Calcule l'intégrale analytique du polynôme de degré 3 sur [a, b].
    - rectangles: Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec la méthode des rectangles.
    - trapezes: Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec  la méthode des trapèzes.

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


# Méthode des rectangles
def rectangles(p, a, b, n=10):
    """
    Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec la méthode des rectangles.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)

    Retour:
    integrale (float) : valeur approximative de l'intégrale de f(x) sur [a, b] par la méthode des rectangles
    """
    pas = (b - a) / n
    integrale = 0
    for i in range(n):
        x = a + (i + 0.5) * pas
        integrale += f(p, x) * pas
    return integrale


# Méthode des trapèzes
def trapezes(p, a, b, n=10):
    """
    Calcule l'intégrale du polynôme de degré 3 sur [a, b] avec la méthode des trapèzes.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)

    Retour:
    integrale (float) : valeur approximative de l'intégrale de f(x) sur [a, b] par la méthode des trapèzes
    """
    pas = (b - a) / n
    integrale = (f(p, a) + f(p, b)) / 2
    for i in range(1, n):
        x = a + i * pas
        integrale += f(p, x)
    integrale *= pas
    return integrale
