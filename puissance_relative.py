"""
puissance_relative.py

Implémente la notion de "puissance relative" entre deux grandeurs A et B.

1. Version analytique :     x = ln(B) / ln(A)
2. Version algorithmique :  recherche progressive de x tel que A**x ≈ B
"""

import math
from typing import Tuple, List


class PuissanceRelativeError(Exception):
    """Exception spécifique pour les erreurs de puissance relative."""
    pass


def puissance_relative_analytique(A: float, B: float) -> float:
    """
    Calcule la puissance relative x telle que A**x = B, via les logarithmes.

    Paramètres
    ----------
    A : float
        Base de référence (doit être > 0 et != 1).
    B : float
        Valeur cible (doit être > 0).

    Retour
    ------
    float
        Exposant x tel que A**x = B.

    Lève
    ----
    PuissanceRelativeError
        Si les conditions sur A et B ne sont pas satisfaites.
    """
    if A <= 0 or A == 1:
        raise PuissanceRelativeError(
            f"A doit être > 0 et != 1 pour définir ln(A). Reçu A={A}."
        )
    if B <= 0:
        raise PuissanceRelativeError(
            f"B doit être > 0 pour définir ln(B). Reçu B={B}."
        )

    return math.log(B) / math.log(A)


def puissance_relative_iterative(
    A: float,
    B: float,
    epsilon: float = 1e-6,
    pas_initial: float = 0.1,
    max_iterations: int = 1_000_000
) -> Tuple[float, List[float]]:
    """
    Approche itérative de la puissance relative x telle que A**x ≈ B.

    Stratégie :
    - on part de x = 0, avec un pas donné
    - on augmente (ou diminue) x par pas jusqu'à "dépasser" la cible
    - on réduit le pas d'un facteur 10
    - on répète jusqu'à ce que |A**x - B| <= epsilon ou que max_iterations soit atteint

    Paramètres
    ----------
    A : float
        Base de référence (doit être > 0 et != 1).
    B : float
        Valeur cible (doit être > 0).
    epsilon : float, optionnel
        Tolérance sur |A**x - B|.
    pas_initial : float, optionnel
        Pas initial d'exploration de l'exposant.
    max_iterations : int, optionnel
        Nombre maximal d'itérations pour éviter les boucles infinies.

    Retour
    ------
    (x, historiques_x) : Tuple[float, List[float]]
        x : approximation de l'exposant tel que A**x ≈ B
        historiques_x : liste des valeurs successives de x (chemin d'ajustement)

    Lève
    ----
    PuissanceRelativeError
        Si les conditions sur A et B ne sont pas satisfaites ou en cas de non-convergence.
    """
    if A <= 0 or A == 1:
        raise PuissanceRelativeError(
            f"A doit être > 0 et != 1 pour définir une puissance exponentielle stable. Reçu A={A}."
        )
    if B <= 0:
        raise PuissanceRelativeError(
            f"B doit être > 0 pour viser A**x ≈ B dans ce cadre. Reçu B={B}."
        )
    if epsilon <= 0:
        raise PuissanceRelativeError("epsilon doit être strictement positif.")
    if pas_initial <= 0:
        raise PuissanceRelativeError("pas_initial doit être strictement positif.")

    x = 0.0
    pas = pas_initial
    historiques_x: List[float] = [x]

    def ecart(val_x: float) -> float:
        return abs(A ** val_x - B)

    current_error = ecart(x)
    iterations = 0

    # On détermine si on doit monter ou descendre en fonction de la première tendance
    # On teste un petit pas positif et négatif pour choisir une direction initiale.
    test_plus = ecart(x + pas)
    test_moins = ecart(x - pas)

    if test_plus < current_error and test_plus <= test_moins:
        direction = 1.0
    elif test_moins < current_error:
        direction = -1.0
    else:
        # Si ni plus ni moins n'améliore la situation de façon claire, on garde + par défaut
        direction = 1.0

    while current_error > epsilon and iterations < max_iterations:
        iterations += 1

        # On avance dans la direction choisie
        nouvel_x = x + direction * pas
        nouvel_ecart = ecart(nouvel_x)

        if nouvel_ecart < current_error:
            # On accepte le nouveau x, l'erreur diminue
            x = nouvel_x
            current_error = nouvel_ecart
            historiques_x.append(x)
        else:
            # On a dépassé ou on ne s'améliore plus : on réduit le pas
            pas /= 10.0
            # On inverse la direction pour explorer l'autre côté
            direction *= -1.0

            # Si le pas devient trop petit, on peut considérer qu'on a convergé
            if pas < 1e-15:
                break

    if current_error > epsilon:
        raise PuissanceRelativeError(
            f"L'algorithme n'a pas convergé dans la tolérance {epsilon} "
            f"après {iterations} itérations. Dernier écart = {current_error}."
        )

    return x, historiques_x


if __name__ == "__main__":
    # Exemple d'utilisation simple
    A_exemple = 2.0
    B_exemple = 10.0

    print(f"Exemple : trouver x tel que {A_exemple}**x = {B_exemple}")

    # Version analytique
    x_ana = puissance_relative_analytique(A_exemple, B_exemple)
    print(f"Puissance relative analytique : x = {x_ana}")

    # Version itérative
    x_it, chemin = puissance_relative_iterative(A_exemple, B_exemple, epsilon=1e-8)
    print(f"Puissance relative itérative  : x = {x_it}")
    print(f"Longueur du chemin d'ajustement : {len(chemin)} étapes")
