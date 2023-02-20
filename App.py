import Tableau

class App:
    #constantes
    TAILLE = 10

    #création du tableau de base
    tableau = Tableau.Tableau(TAILLE)
    tableau.fillTab()
    #affichage du résultat
    tableau.show()