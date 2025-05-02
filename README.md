# Projet Base d'IA – Probleme des 8 Reines

##  Objectif

Placer **8 reines sur un echiquier 8x8** de maniere  **qu’aucune ne se menace** :


comme que la reine peut se déplacer dans trois directions :

Horizontalement (sur la meme ligne)

Verticalement  (sur la meme colonne)

Diagonalement  (sur les diagonales)

Donc on doit :
 Éviter deux reines sur la meme ligne
Sinon une attaque horizontalement 

Éviter deux reines sur la meme colonne
Sinon un attaque verticalement 

 Éviter deux reines sur une diagonale
Sinon un attaque en diagonale 
---



## Comment fonctionne la solution ?

Le programme utilise un **algorithme simple appele "recherche en profondeur" (DFS)** avec **backtracking** :

1. On place une reine ligne par ligne.
2. A chaque position, on verifie :
   - si la case est sure pas d’autre reine en conflit
3. Si c’est bon, on continue avec la ligne suivante
4. Sinon, on **retire la derniere reine** et on essaye un autre emplacement

On repete **jusqu’a trouver une solution complete**

---

##  Exemple de solution affichée

Le resultat final est affiché  sous forme d’echiquier :  

