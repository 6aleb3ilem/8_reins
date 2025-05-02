# Projet Base d'IA – Probleme des 8 Reines

##  Objectif

Placer **8 reines sur un echiquier 8x8** de maniere  **qu’aucune ne se menace** :
![Screenshot from 2025-05-02 12-42-54](https://github.com/user-attachments/assets/b42569b7-fa84-4109-97a2-916ccd147add)
![Screenshot from 2025-05-02 12-43-40](https://github.com/user-attachments/assets/007e8cc6-e6f5-4ff5-a35b-ef71639e3676)


comme que la reine peut se déplacer dans trois directions :

Horizontalement (sur la meme ligne)

Verticalement  (sur la meme colonne)

Diagonalement  (sur les diagonales)

Donc on doit :
 -Eviter deux reines sur la meme ligne
Sinon une attaque horizontalement 

-Eviter deux reines sur la meme colonne
Sinon un attaque verticalement 

 -Eviter deux reines sur une diagonale
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
![image](https://github.com/user-attachments/assets/35179472-7040-4301-bc60-2b3bd3dc655d)


