from time import sleep
import datetime

contact_tab = []

def Contact():
    while True:
        nom = input("Entrez le Nom : ")
        prenom = input("Entrez le Prénom : ")
        date_str = input("Entrez la date d'anniversaire (aaaa/mm/jj) : ")
        date = datetime.datetime.strptime(date_str, "%Y/%m/%d")
        
        contact_tab.append({"nom": nom, "prenom": prenom, "date": date})
        
        choix = input("Voulez-vous continuer ? (y/n) : ")
        if choix.lower() == "n":
            break

def main():
    print("Formulaire de Contact")
    sleep(1)
    Contact()
    
    contact_tab.sort(key=lambda x: x["date"], reverse=True)
    
    print("\nContacts triés par date d'anniversaire décroissante:")
    for contact in contact_tab:
        print(f"Nom: {contact['nom']}, Prénom: {contact['prenom']}, Date d'anniversaire: {contact['date'].strftime('%Y/%m/%d')}")

if __name__ == "__main__":
    main()
