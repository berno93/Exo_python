# Met le chiffre qui se situe à l'index N en 1ere position

list_nb = []
N = ""

while True:
        liste = input("Entrez une liste de mot ou/et de nombres : ")
        if liste == "":
            break
        list_nb.append(liste)

    N = int(input("Saissisez un chiffre (index) : "))

def rot(list_nb, N):
    rot_list = []
    buffer = ""
    for element, n in enumerate(list_nb):
        buffer= element
        element = rot_list.appen(list_nb[n-1])
    return rot_list

rot(list_nb, N)