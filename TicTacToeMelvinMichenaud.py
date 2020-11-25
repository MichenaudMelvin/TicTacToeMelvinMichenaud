grille = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
joueur = "X"

def initialiseGrille(grille):
    for compteur in range(0,9):
        grille[compteur] = "_"

def afficheGrille(grille):
    for i in range(0,3):
        print(grille[3*i], grille[3*i+1], grille[3*i+2],"\n")

def ajouteSymbole(grille, joueur):
    choixIncorrect = True
    while choixIncorrect == True:
        i = int(input("Sur quelle ligne voulez-vous jouer ?"))
        j = int(input("Sur quelle colonne voulez-vous jouer ?"))
        if grille[3*i+j] == "_":
            grille[3*i+j] = joueur
            choixIncorrect = False
        if i >= 3 or j >= 3:
            print("veuillez saisir un chiffre entre 0 et 2")

def testVictoireVerticale(grille):
    compteur = 0
    while compteur < 3:
        if grille[compteur] != "_" and grille[compteur] == grille[compteur+3] and grille[compteur] == grille[compteur+6]:
            victoire = True
        else:
            victoire = False
        compteur = compteur+1
    return(victoire)

def testVictoireHorizontale(grille):
    compteur = 0
    while compteur < 3:
        if grille[compteur] != "_" and grille[compteur*3] == grille[compteur*3+1] and grille[compteur*3] == grille[compteur*3+2]:
            victoire = True
        else:
            victoire = False
        compteur = compteur+1
    return(victoire)

def testVictoireDiagonale(grille):
    compteur = 0
    if grille[4] == grille[0] and grille[4] == grille[8]:
        victoire = True
    if grille[4] == grille[2] and grille[4] == grille[6]:
        victoire = True
    else:
        victoire = False
    return(victoire)

initialiseGrille(grille)
afficheGrille(grille)
ajouteSymbole(grille, joueur)
afficheGrille(grille)
ajouteSymbole(grille, joueur)
afficheGrille(grille)
ajouteSymbole(grille, joueur)
afficheGrille(grille)
victoire = testVictoireDiagonale(grille)
print(victoire)

input()
