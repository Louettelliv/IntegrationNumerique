"""
Module de comparaison des méthodes d'intégration numériques

Ce module permet de comparer différentes méthodes d'intégration numérique pour un polynôme de degré 3.
Les méthodes de comparaison incluent le calcul de l'erreur, l'analyse de la convergence, et la mesure du temps
d'exécution.

Fonctions:
    - erreur_absolue: Calcule l'erreur absolue entre l'intégrale analytique et l'intégrale numérique.
    - erreur_integration: Retourne l'erreur absolue pour un nombre donné de segments.
    - temps_execution: Mesure le temps d'exécution d'une méthode d'intégration.
    - plot_erreur: Affiche un histogramme des erreurs pour différentes méthodes et différents nombres de segments.
    - plot_convergence: Affiche la convergence des différentes méthodes d'intégration en fonction du nombre de segments.
    - plot_temps_execution: Affiche un graphique du temps d'exécution des méthodes en fonction du nombre de segments.
    - resulat: Affiche les résultats des méthodes d'intégration, y compris l'erreur et le temps d'exécution.
    - methodes_a_comparer: Retourne un dictionnaire des méthodes d'intégration à comparer.

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


def plot_erreur(p, a, b, segments, methodes):
    """
    Affiche un histogramme des erreurs d'intégration pour différentes méthodes et différents nombres de segments.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    segments (list) : liste du nombre de segments à utiliser
    methodes (dict) : dictionnaire des méthodes d'intégration
    """
    bar_width = 0.2  # Largeur des barres de l'histogramme
    index = np.arange(len(methodes))  # Positions des groupes sur l'axe des x

    plt.figure()

    for i, n in enumerate(segments):
        erreurs = [erreur_integration(p, a, b, info['fonction'], n) for info in methodes.values()]
        bar_positions = index + i * bar_width  # Calcul des positions des barres
        plt.bar(bar_positions, erreurs, bar_width, label=f'{n} Segments')

    plt.xlabel("Méthode d'intégration")
    plt.ylabel("Erreur d'intégration")
    plt.yscale('log')
    plt.title('Erreurs par méthode et par nombre de segments')
    plt.xticks(index + bar_width * (len(segments) - 1) / 2, list(methodes.keys()))
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()


# Fonction pour vérifier la convergence
def plot_convergence(p, a, b, segments, methodes):
    """
    Affiche la convergence des différentes méthodes d'intégration en fonction du nombre de segments.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    segments (list) : liste du nombre de segments à utiliser
    methodes (dict) : dictionnaire des méthodes d'intégration
    """
    plt.figure()
    for nom_methode, info in methodes.items():
        methode = info['fonction']
        linestyle = info['linestyle']
        erreurs = [erreur_integration(p, a, b, methode, n) for n in segments]
        plt.plot(segments, erreurs, label=nom_methode, linestyle=linestyle)
    plt.xlabel('Nombre de segments')
    plt.xscale('log')
    plt.ylabel("Erreur d'intégration")
    plt.yscale('log')
    plt.title("Convergence des différentes méthodes d'intégration")
    plt.legend()
    plt.grid(True)
    plt.show()

# Graphiques de temps d'exécution
def plot_temps_execution(p, a, b, segments, methodes):
    """
    Affiche un graphique du temps d'exécution des différentes méthodes en fonction du nombre de segments.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    segments (list) : liste du nombre de segments à utiliser
    methodes (dict) : dictionnaire des méthodes d'intégration
    """
    plt.figure()
    for nom_methode, info in methodes.items():
        methode = info['fonction']
        linestyle = info['linestyle']
        times = [temps_execution(methode, p, a, b, n) for n in segments]
        plt.plot(segments, times, label=nom_methode, linestyle=linestyle)
    plt.xlabel('Nombre de segments')
    plt.xscale('log')
    plt.ylabel("Temps d'exécution (s)")
    plt.yscale('log')
    plt.title("Temps d'exécution des différentes méthodes d'intégration")
    plt.legend()
    plt.grid(True)
    plt.show()


# Résultats des méthodes
def resulat(p, a, b, methodes, n=10):
    """
    Affiche les résultats des méthodes d'intégration, y compris l'erreur et le temps d'exécution.

    Arguments:
    p (list) : liste des coefficients du polynôme
    a, b (float) : bornes de l'intervalle d'intégration
    n (int) : nombre de segments (10 par défaut)
    methodes (dict) : dictionnaire des méthodes d'intégration
    """
    analytique = methodes_python.analytique(p, a, b)
    for nom_methode, info in methodes.items():
        methode = info['fonction']
        numerique = methode(p, a, b, n)
        erreur = erreur_absolue(analytique, numerique)
        tps_execution = temps_execution(methode, p, a, b, n)
        print(f"{nom_methode}: I = {numerique:.3f}, Erreur = {erreur:.3e}, Temps d'exécution = {tps_execution:.3e}")


# Méthodes à comparer
def methodes_a_comparer():
    """
    Retourne un dictionnaire des méthodes d'intégration à comparer, avec leurs styles de ligne pour les graphiques.

    Retour:
    methodes (dict) : dictionnaire contenant les méthodes d'intégration et leurs styles de ligne
    """
    methodes = {
        'Rectangles (Base)': {'fonction': methodes_python.rectangles, 'linestyle': '-'},
        'Rectangles (NumPy)': {'fonction': methodes_numpy.rectangles, 'linestyle': '--'},
        'Trapèzes (Base)': {'fonction': methodes_python.trapezes, 'linestyle': '-'},
        'Trapèzes (NumPy)': {'fonction': methodes_numpy.trapezes, 'linestyle': '--'},
        'Trapèzes (SciPy)': {'fonction': methodes_scipy.trapezes, 'linestyle': ':'},
        'Simpson (Base)': {'fonction': methodes_python.simpson, 'linestyle': '-'},
        'Simpson (NumPy)': {'fonction': methodes_numpy.simpson, 'linestyle': '--'},
        'Simpson (SciPy)': {'fonction': methodes_scipy.smpson, 'linestyle': ':'}
        }
    return methodes
