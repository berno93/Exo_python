def fibonaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

try:
    n = int(input("Entrez un nombre : "))
    if n < 0:
        print("Le nombre doit être positif.")
    else:
        result = fibonaci(n)
        print(f"Le",n,"-ième terme de la suite de Fibonacci est :",result)
except ValueError:
    print("Veuillez entrer un nombre entier.")