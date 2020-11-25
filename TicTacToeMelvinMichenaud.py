#fonctions
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
            finJeu = True
        else:
            victoire = False
            finJeu = False
        compteur = compteur+1
    return(victoire, finJeu)

def testVictoireHorizontale(grille):
    compteur = 0
    while compteur < 3:
        if grille[compteur] != "_" and grille[compteur*3] == grille[compteur*3+1] and grille[compteur*3] == grille[compteur*3+2]:
            victoire = True
            finJeu = True
        else:
            victoire = False
            finJeu = False
        compteur = compteur+1
    return(victoire, finJeu)

def testVictoireDiagonale(grille):
    if grille[4] != "_":
        if grille[4] == grille[0] == grille[8] or grille[4] == grille[2] == grille[6]:
            victoire = True
            finJeu = True
        else:
            victoire = False
            finJeu = False
    return(victoire, finJeu)

def testJeuNul(tour, victoire):
    if tour == 9 and victoire == False:
        finJeu = True
    else:
        finJeu = False
    return(finJeu)

#debut programme
grille = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
joueur = "X"
tour = 0
finJeu = False

initialiseGrille(grille)
while finJeu != True:
    afficheGrille(grille)
    ajouteSymbole(grille, joueur)
    victoire = testVictoireVerticale(grille)[0]
    finJeu = testVictoireVerticale(grille)[1]
    
    victoire = testVictoireHorizontale(grille)[0]
    finJeu = testVictoireHorizontale(grille)[1]
    
    victoire = testVictoireDiagonale(grille)[0]
    finJeu = testVictoireDiagonale(grille)[1]
    
    finJeu = testJeuNul(tour, victoire)
    tour = tour + 1

input()
