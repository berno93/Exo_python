def draw_pyramid(height):
    for i in range(1, height + 1):
        for _ in range(height - i):
            print(" ", end="")
        for _ in range(1, i * 2):
            print("-", end="")
        print()

try:
    num_levels = int(input("Entrez le nombre d'étages de la pyramide : "))
    if num_levels < 1:
        print("Le nombre d'étages doit être supérieur ou égal à 1.")
    else:
        draw_pyramid(num_levels)
except ValueError:
    print("Veuillez entrer un nombre entier.")
