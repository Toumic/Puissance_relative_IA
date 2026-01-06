# Puissance relative

Ce dépôt explore la notion de **puissance relative** entre deux grandeurs, c’est‑à‑dire l’exposant `x` tel que :



\[
A^x = B
\]



Plutôt que de se contenter de différences (`B - A`) ou de ratios (`B / A`), la puissance relative propose une mesure **exponentielle** de la relation entre une base `A` et une cible `B`.

Le projet contient :

- une **définition analytique** : `x = ln(B) / ln(A)`
- une **procédure algorithmique** : exploration itérative de `x` par raffinements successifs
- une interprétation conceptuelle : la relation comme **trajet d’ajustement**, pas seulement comme écart statique.

---

## Contenu

- `puissance_relative.py`  
  Implémente :
  - `puissance_relative_analytique(A, B)`  
    Calcule directement l’exposant `x` via les logarithmes.
  - `puissance_relative_iterative(A, B, epsilon, pas_initial, max_iterations)`  
    Approche `x` par un processus d’ajustement progressif, en mémorisant les étapes.

---

## Installation

Aucune dépendance externe n’est requise, à part Python (>= 3.8 recommandé).

```bash

git clone <URL_DU_DEPOT>
cd puissance-relative
python3 puissance_relative.py

## Licence

Ce projet utilise une double licence adaptée à sa nature hybride :

- **Code Python** : licence MIT — librement réutilisable, modifiable et distribuable.
- **Contenus conceptuels** (théorie, article, manifeste, schémas, explications) :
  licence **Creative Commons BY‑NC‑SA 4.0** — utilisation autorisée, 
  mais sans usage commercial et avec obligation de partage dans les mêmes conditions.

Cette combinaison protège la paternité intellectuelle de la théorie de la 
*Puissance Relative* tout en permettant au code de circuler librement.
