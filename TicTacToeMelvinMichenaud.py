grille = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
joueur = "X"
victoire = False

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

def testVictoireVerticale(grille, victoire):
    compteur = 0
    for compteur in range (0,3):
        if grille[compteur] != "_" and grille[compteur] == grille[compteur+3] and grille[compteur] == grille[compteur+6]:
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
ajouteSymbole(grille, joueur)
afficheGrille(grille)
testVictoireVerticale(grille)
print(victoire)

input()
