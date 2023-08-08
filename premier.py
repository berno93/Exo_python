def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    N = int(input("Entrez un nombre N : "))
    if N < 2:
        print("Aucun nombre premier dans cet intervalle.")
    else:
        print(f"Les nombres premiers entre 0 et {N} sont :")
        for num in range(2, N + 1):
            if is_prime(num):
                print(num, end=" ")
except ValueError:
    print("Veuillez entrer un nombre entier.")
