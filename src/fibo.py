def fibonacci(n):
    """Calcule le n ième terme de la suite de Fibonacci
    en utilisant un algorithme récursif.
    """ 
    if n < 2:
        return 1
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range (1, 15):
        print(fibonacci(i))