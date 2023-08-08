# Met le chiffre qui se situe à l'index N en 1ere position

list_nb = []
N = ""

def rot(list_nb, N):
    while True:
        liste = input("Entrez une liste de mot ou/et de nombres : ")
        if liste == "":
            break
        list_nb.append(liste)

    N = int(input("Saissisez un chiffre (index) : "))
    add = list_nb[N]
    list_nb.insert(0, add)
    list_nb.pop(N+1)
    print(list_nb)


rot(list_nb, N)