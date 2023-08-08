list_tab = []
index=""

while True:
    liste = input("Saississez une liste de mot ou de Nombres (appuyer sur Entrée pour terminer) : ")
    if liste == "":
        break
    list_tab.append(liste)


def get_last_n_index(list_tab, index):
    list_tab.reverse()
    index = int(input("Quel élément de l'index souhaitez vous avoir ? : "))
    
    if index > len(list_tab):
        print("Aucun élément trouver")
    else:
        print("L'élément qui se trouve à l'index",index,"de votre liste est :",list_tab[index]) 
  
get_last_n_index(list_tab, index)
