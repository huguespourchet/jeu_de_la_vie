import Tableau

class App:
    #constantes
    TAILLE = 10

    def main(taille):
        #création du tableau de base
        tableau = Tableau.Tableau(taille)
        tableau.fillTab()
        #affichage du résultat
        tableau.show()
        
    main(TAILLE)
        
