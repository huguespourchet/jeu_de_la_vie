import random
TAILLE = 10

init_tab()


def init_tab():

    a = [[0] * taille] * taille
    for i in range(taille):
        for j in range(taille):
            a[i][j] = int(random.randint(0, 1))