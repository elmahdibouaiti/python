import math

a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("L'équation a deux solutions réelles sont :", x1, "et", x2)
elif discriminant == 0:
    x = -b / (2*a)
    print("L'équation a une seule solution réelle :", x)
else:
    print("L'équation n'a pas de solution réelle dans R.")

