print("Renseignez la longueur de votre rectangle")
longueur= float(input())
print("Renseignez la largeur de votre rectangle")
largeur= float(input())

def square_area(longueur, largeur):
    return  longueur*largeur

area = square_area(longueur, largeur)
print("Le rectangle de longueur :",longueur, "et de largeur :",largeur, "a une aire de :", area)