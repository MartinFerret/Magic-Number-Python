

from random import randint


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = randint(1,10)

def demander_nb_magique(min, max):
    nombre_str = input(f"Quel est le nombre magique (entre {min} et {max}) ?")
    try:
        nombre_int = int(nombre_str)
    except:
        print("ERREUR: Vous devez rentrer un nombre")
    return nombre_int

nombre = 0

while not nombre == NOMBRE_MAGIQUE:
    nombre = demander_nb_magique(NOMBRE_MIN, NOMBRE_MAX)
    if nombre > NOMBRE_MIN and nombre < NOMBRE_MAX:
        if nombre < NOMBRE_MAGIQUE:
            print("Votre nombre est trop petit")
        elif nombre > NOMBRE_MAGIQUE:
            print("Votre nombre est trop grand")
        elif nombre == NOMBRE_MAGIQUE:
            print("Vous avez deviné, bravo !")
    else:
        print(f"Votre nombre n'est pas compris entre {NOMBRE_MIN} et {NOMBRE_MAX}")

    


