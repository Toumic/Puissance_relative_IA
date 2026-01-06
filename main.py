# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from puissance_relative_analytique import puissance_relative_analytique
from puissance_relative_iterative import puissance_relative_iterative


def main():
    print("=== Calcul de puissance relative ===")

    # Exemple de valeurs
    a = 2
    b = 16

    print(f"\nValeurs utilisées : a = {a}, b = {b}")

    # Méthode analytique
    try:
        resultat_analytique = puissance_relative_analytique(a, b)
        print(f"\nMéthode analytique : {resultat_analytique}")
    except Exception as e:
        print(f"\nMéthode analytique indisponible : {e}")

    # Méthode itérative
    try:
        resultat_iteratif = puissance_relative_iterative(a, b)
        print(f"Méthode itérative : {resultat_iteratif}")
    except Exception as e:
        print(f"Méthode itérative indisponible : {e}")


if __name__ == "__main__":
    main()
