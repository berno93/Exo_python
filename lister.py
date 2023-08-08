word_tab = []

while True:
    word = input("Saississez une liste de mot (appuyer sur Entrée pour terminer) : ")
    if word == "":
        break
    word_tab.append(word)
    
word_tab.reverse()
print(word_tab) 