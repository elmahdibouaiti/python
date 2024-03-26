def nbCarMaj(p):
    compt = 0
    for car in p:
        if car.isupper():
            compt += 1
    return compt


pt = input("Entrez une phrase: ")
print("Nombre de majuscules:", nbCarMaj(pt))
