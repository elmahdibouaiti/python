""" Excercice1 """
a,b = 12,16.5
print("a = ",a)
print("b = ",b)

""" Excercice2 """

nb1 = int(input("Entrer le primier nombre"))
nb2 = int(input("Entrer le deuxieme nombre"))

s = nb1 + nb2 
m =  nb1 * nb2

print("Somme : ",s)
print("multiplication : ",m)

""" Excercice3 """
nb1 = int(input("Entrer le primier nombre"))
nb2 = int(input("Entrer le deuxieme nombre"))

if nb2 == 0:
    print ("Impossible de diviser par zero")
else:
    q = nb1 // nb2
    r = nb1 % nb2
    print("Le quotient est",q,"et le reste est",r)


""" Excercice4 """

x = int(input("Entrez le premier entier: "))
y = int(input("Entrez le deuxième entier: "))
z = int(input("Entrez le troisième entier: "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("Les entiers classés par ordre croissant sont:", x, y, z)


