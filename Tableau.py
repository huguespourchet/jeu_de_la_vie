import random

class Tableau:

    matrice = []
    taille = 0

    def __init__(self, taille):
        self.matrice = [[0] * taille] * taille
        self.taille = taille
    
    def fillTab(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.matrice[i][j] = int(random.randint(0, 1))
    
    def show(self):
        print(self.matrice)