def triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))


n = int(input("Entrez la taille du triangle: "))
triangle(n)
