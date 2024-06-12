# Intégration numérique de polynômes de degré 3

Ce projet fournit plusieurs modules pour calculer l'intégrale d'un polynôme de degré 3 sur un intervalle donné [a, b]. Les méthodes implémentées incluent des approches de base en Python, des méthodes vectorisées utilisant NumPy, et des méthodes optimisées via SciPy. Ce projet comprend également des outils pour comparer l'efficacité et la précision de ces méthodes.

## Table des Matières

- [Contenu](#contenu)
- [Structure](#modules)
  - [methodes_python.py](#methodes_pythonpy)
  - [methodes_numpy.py](#methodes_numpypy)
  - [methodes_scipy.py](#methodes_scipypy)
  - [comparaisons.py](#comparaisonspy)
  - [main.py](#mainpy)
- [Utilisation](#utilisation)
- [Auteurs](#auteurs)

## Contenu
Ce répertoire contient :
- 4 modules :
    - methodes_python.py
    - methodes_numpy.py
    - methodes_scipy.py
    - comparaisons.py
- Un fichier main.py à exécuter
- Un fichier README.md

## Structure

### methodes_python.py
Ce module implémente les méthodes d'intégration en utilisant Python de base.

#### Fonctions :
- `f(p, x)`: Calcule la valeur du polynôme de degré 3 à un point x donné.
- `analytique(p, a, b)`: Calcule l'intégrale analytique du polynôme sur [a, b].
- `rectangles(p, a, b, n=10)`: Calcule l'intégrale par la méthode des rectangles.
- `trapezes(p, a, b, n=10)`: Calcule l'intégrale par la méthode des trapèzes.
- `simpson(p, a, b, n=10)`: Calcule l'intégrale par la méthode de Simpson.

### methodes_numpy.py
Ce module implémente des méthodes d'intégration vectorisées utilisant NumPy.

#### Fonctions :
- `f(p, x)`: Calcule la valeur du polynôme de degré 3 à un point x donné.
- `rectangles(p, a, b, n=10)`: Calcule l'intégrale par la méthode des rectangles vectorisée.
- `trapezes(p, a, b, n=10)`: Calcule l'intégrale par la méthode des trapèzes vectorisée.
- `simpson(p, a, b, n=10)`: Calcule l'intégrale par la méthode de Simpson vectorisée.

### methodes_scipy.py
Ce module utilise SciPy pour des méthodes d'intégration optimisées.

#### Fonctions :
- `f(p, x)`: Calcule la valeur du polynôme de degré 3 à un point x donné.
- `trapezes(p, a, b, n=10)`: Calcule l'intégrale par la méthode des trapèzes de SciPy.
- `smpson(p, a, b, n=10)`: Calcule l'intégrale par la méthode de Simpson de SciPy.

### comparaisons.py
Ce module compare les différentes méthodes d'intégration numérique. Il inclut des fonctions pour mesurer l'erreur, analyser la convergence et mesurer le temps d'exécution.

#### Fonctions :
- `methodes_a_comparer()`: Retourne un dictionnaire des méthodes d'intégration à comparer.
- `erreur_absolue(analytique, numerique)`: Calcule l'erreur absolue entre l'intégrale analytique et numérique.
- `erreur_integration(p, a, b, methode, n=10)`: Retourne l'erreur pour un nombre donné de segments.
- `plot_erreur(p, a, b, segments, methodes)`: Affiche un histogramme des erreurs d'intégration.
- `plot_convergence(p, a, b, segments, methodes)`: Affiche la convergence des différentes méthodes d'intégration.
- `temps_execution(methode, p, a, b, n=10)`: Mesure le temps d'exécution d'une méthode d'intégration.
- `plot_temps_execution(p, a, b, segments, methodes)`: Affiche un graphique du temps d'exécution des méthodes.
- `resulat(p, a, b, methodes, n=10)`: Affiche les résultats des méthodes d'intégration.

### main.py
Ce fichier exécute les comparaisons entre les différentes méthodes d'intégration numérique pour une fonction polynomiale de degré 3. Il affiche les résultats et génère les graphiques de convergence, de temps d'exécution et des erreurs.

## Utilisation

1. Clonez ou télécharger l'ensemble de ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python 3 installé sur votre système.
3. Installez les dépendances nécessaires :
    ```bash
    pip install numpy scipy matplotlib
    ```
4. Exécutez le programme en exécutant le fichier `main.py`.

Vous pouvez modifier les coefficients du polynôme et les bornes d'intégration dans la fonction `main()` du fichier main.py

## Auteurs

Ce programme a été développé par [Lou-Anne Villette](https://github.com/Louettelliv) et [Thomas Chambeyron](https://github.com/ThomasChambeyron).
