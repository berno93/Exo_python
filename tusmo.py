import random
import os

# Liste de mots prédéfinis
word_list = ["python", "program", "game", "color", "terminal", "random", "letter", "position", "manche"]

def pick_random_word():
    return random.choice(word_list)

def display_board(attempts, guesses):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    print(f"Manche {attempts + 1}/5")
    print("-------------")

    for i in range(5):
        if i < attempts:
            print(f"{guesses[i]['letter']} - {guesses[i]['color']}")
        else:
            print("")

def main():
    word_to_guess = pick_random_word()
    first_letter = word_to_guess[0]
    attempts = 0
    guesses = [{'letter': first_letter, 'color': '\033[91mR\033[0m'} for _ in range(5)]

    while attempts < 5:
        display_board(attempts, guesses)
        user_guess = input("Devinez le mot: ").lower()

        if user_guess == word_to_guess:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Bravo, vous avez trouvé le mot : {word_to_guess}")
            break

        for i in range(len(user_guess)):
            if user_guess[i] == word_to_guess[i]:
                guesses[attempts]['color'] = '\033[91mR\033[0m'
            elif user_guess[i] in word_to_guess:
                guesses[attempts]['color'] = '\033[93mJ\033[0m'

        attempts += 1

    display_board(attempts, guesses)
    if attempts == 5:
        print(f"Le mot à deviner était : {word_to_guess}")

if __name__ == "__main__":
    main()
