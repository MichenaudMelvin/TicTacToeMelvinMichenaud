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

def testVictoireVerticale(grille, finJeu):
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

def testVictoireHorizontale(grille, finJeu):
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

def testVictoireDiagonale(grille, finJeu):
    if grille[4] != "_":
        if grille[4] == grille[0] == grille[8] or grille[4] == grille[2] == grille[6]:
            victoire = True
            finJeu = True
        else:
            victoire = False
            finJeu = False
    print(victoire)
    return(victoire, finJeu)

def testJeuNul(tour, finJeu):
    if tour == 8 and victoire == False:
        finJeu = True
    else:
        finJeu = False
    return(finJeu)

#debut programme
grille = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
joueur = "X"
tour = 0
finJeu = False
victoire = 0
victoire1 = False
victoire2 = False
victoire3 = False

initialiseGrille(grille)
while finJeu != True or victoire1 == True or victoire2 == True or victoire3 == True:
    afficheGrille(grille)
    ajouteSymbole(grille, joueur)
    
    victoire1 = testVictoireVerticale(grille, finJeu)[0]
    finJeu = testVictoireVerticale(grille, finJeu)[1]
    print(victoire1)
    
    victoire2 = testVictoireHorizontale(grille, finJeu)[0]
    finJeu = testVictoireHorizontale(grille, finJeu)[1]
    print(victoire2)
    
    victoire3 = testVictoireDiagonale(grille, finJeu)[0]
    finJeu = testVictoireDiagonale(grille, finJeu)[1]
    print(victoire3)
    
    finJeu = testJeuNul(tour, finJeu)
    tour = tour + 1
    print(tour)

print('sortie de la boucle')
input()
