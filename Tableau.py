import random

class Tableau:

    matrice = []
    col = 0
    line = 0

    def __init__(self, col, line):
        for i in range(line):
            ligne = []
            for j in range(col):
                ligne.append(0)
            self.matrice.append(ligne)

        self.col, self.line = col, line
    
    def fillTab(self):
        for i in range(self.line):
            for j in range(self.col):
                self.matrice[i][j] = int(random.randint(0, 1))
    
    def show(self):
        for i in range(self.line):
            for j in range(self.col):
                if self.matrice[i][j] == 1:
                    print("O ", end="")
                else:
                    print("  ", end="")
            print()

    def checkNeighboors(self):
        mat = []
        for i in range(self.line):
            for j in range(self.col):
                compteur = 0
                try:
                    if self.matrice[i][j-1] == 1:
                        compteur +=1
                    if self.matrice[i-1][j-1] == 1:
                        compteur +=1
                        print(2)
                    if self.matrice[i-1][j] == 1:
                        compteur +=1
                        print(3)
                    if self.matrice[i-1][j+1] == 1:
                        compteur +=1
                        print(3)
                    if self.matrice[i][j+1] == 1:
                        compteur +=1
                        print(4)
                    if self.matrice[i+1][j+1] == 1:
                        compteur +=1
                        print(5)
                    if self.matrice[i+1][j] == 1:
                        compteur +=1
                        print(6)
                    if self.matrice[i+1][j-1] == 1:
                        compteur +=1
                        print(7)
                except:
                    compteur = compteur
                mat.append(compteur)
                print(mat)
                exit()
        print(mat)   
