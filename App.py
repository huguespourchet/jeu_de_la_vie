import Tableau

class App:
    #constantes
    COL = 15
    LINE = 10

    def main(col, line):
        #création du tableau de base
        tableau = Tableau.Tableau(col, line)
        tableau.fillTab()
        #affichage du résultat
        tableau.show()
        tableau.checkNeighboors()
        
    main(COL, LINE)
        
