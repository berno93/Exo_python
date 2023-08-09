import random

def jouer_jeu():
    pays_capitales = {
        "France": "Paris",
        "Allemagne": "Berlin",
        "Espagne": "Madrid",
        "Italie": "Rome",
        "Royaume-Uni": "Londres",
        "Portugal": "Lisbonne",
        "Pays-Bas": "Amsterdam",
        "Belgique": "Bruxelles",
        "Suisse": "Berne",
        "Autriche": "Vienne"
    }
    
    points = 0
    
    while True:
        pays = random.choice(list(pays_capitales.keys()))
        capitale_correcte = pays_capitales[pays]
        
        reponse = input(f"Quelle est la capitale de {pays} ? (ou 'q' pour quitter) ")
        
        if reponse.lower() == "q":
            break
        
        if reponse == capitale_correcte:
            points += 1
            print(f"Bravo ! Vous avez gagné 1 point. Total de points : {points}")
        else:
            print(f"Mauvaise réponse. Vous avez obtenu {points} points.")
            break

def main():
    print("Bienvenue dans le jeu des capitales !")
    print("Devinez les capitales des pays proposés.")
    print("Si vous souhaitez quitter le jeu, entrez 'q' comme réponse.\n")
    
    jouer_jeu()

if __name__ == "__main__":
    main()
