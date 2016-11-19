def effaceTableau(tab):
    ''' (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice)
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            tab[i][j] = '-'
    # retourne rien


def verifieGagner(tab):
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!"
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''
    if testMatchNul(tab) is True:
        print("Match nul")
        return True
    for i in ['X', 'O']:
        if testLignes(tab) == i or testCols(tab) == i or testDiags(tab) == i:
            print("Joueur {} a gagné!").format(i)
            return True
    return False


def testLignes(tab):
    ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    # Verifie chaque ligne pour un gangant 'X' ou 'O' et retourne le gangant ou Nul
    for i in range(2):
        if tab[i][0] == tab[i][1] == tab[i][2] == 'O':
            return 'X'
        elif tab[i][0] == tab[i][1] == tab[i][2] == 'X':
            return 'O'
    return '-'  # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant



def testCols(tab):
    ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

    # Verifie chaque colonne pour un gangant 'X' ou 'O' et retourne le gangant ou Nul
    for i in range(2):
        if tab[0][i] == tab[1][i] == tab[2][i] == 'O':
            return 'X'
        elif tab[0][i] == tab[1][i] == tab[2][i] == 'X':
            return 'O'
    return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant


def testDiags(tab):
    ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    # Verifie pour un gagnant 'X' en diagonal ensuite pour un gagnant 'O' en diagonal.
    list =('X','O')
    for i in list:
        if tab[0][0] == tab[1][1] == tab[2][2] == i:
            return i
        elif tab[0][2] == tab[1][1] == tab[2][0] == i:
            return i
    return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant



def testMatchNul(tab):
    '''(list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.
   * Si on ne trouve pas de '-' dans la matrice, retourne True.
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    # return true is '-' est encore dans le tableau, False si tout les position sont occupe soit par un 'X' ou 'O'
    for i in range(2):
        if list[i].count('-') > 0:
            return True
    return False
