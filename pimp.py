from time import sleep

print("Bienvenue dans notre logiciel de Parité")
sleep(1.5)
print("Entrez un nombre")
nb= int(input())

if nb%2 ==0:
    print("Ce nombre est paire")
else:
    print("Ce nombre est impaire")


