from itertools import permutations

def calculate_combinations(numbers):
    all_combinations = list(permutations(numbers))
    total = len(all_combinations)
    return all_combinations, total

sequence = []

while True:
    try:
        num_input = input("Entrez un nombre (ou appuyez sur Entrée pour terminer) : ")
        if num_input == "":
            break
        num = int(num_input)
        sequence.append(num)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

combinations_list, total_combinations = calculate_combinations(sequence)

print("Les combinaisons possibles sont :")
for combo in combinations_list:
    print("".join(str(num) for num in combo), end=" ")
print("\nLe nombre total de combinaisons possibles est :", total_combinations)
