def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    n = int(input("Entrez un nombre : "))
    if n < 0:
        print("Le factoriel n'est pas défini pour les nombres négatifs.")
    else:
        result = factorial(n)
        print("Le factoriel de",n, "est",result)
except ValueError:
    print("Veuillez entrer un nombre entier.")
