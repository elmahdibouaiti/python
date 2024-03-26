def minimum(a, b, c):
    if a <= b and a <= c:
        print("Le plus petit nombre est", a)
    elif b <= a and b <= c:
        print("Le plus petit nombre est", b)
    else:
        print("Le plus petit nombre est", c)


num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))
num3 = float(input("Entrez le troisième nombre: "))
minimum(num1, num2, num3)

