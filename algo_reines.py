# Taille
N = 8

# verifie si une reine peut être placée en (ligne, col)
def est_sure(plateau, ligne, col):
    # verifier les colonnes et diagonales au-dessus
    for i in range(ligne):
        if plateau[i][col] == 1:
            return False  # meme colonne
        if col - (ligne - i) >= 0 and plateau[i][col - (ligne - i)] == 1:
            return False  # Diagonale gauche
        if col + (ligne - i) < N and plateau[i][col + (ligne - i)] == 1:
            return False  # Diagonale droite
    return True

# Place les reines ligne par ligne
def placer_reines(plateau, ligne):
    if ligne == N:
        return True  # Toutes les reines sont placees 

    for col in range(N):
        if est_sure(plateau, ligne, col):
            plateau[ligne][col] = 1  # Place une reine
            if placer_reines(plateau, ligne + 1):  # Essaye la suivante
                return True
            plateau[ligne][col] = 0  # enleve la reine (backtracking)
    return False

# commencons la resolution
def obtenir_solution():
    plateau = [[0] * N for _ in range(N)]  # cree un echiquier vide
    if placer_reines(plateau, 0):
        return plateau
    return None
