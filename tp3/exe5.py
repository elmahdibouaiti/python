def occurrence(p, c):
    return p.count(c)


pt = input("Entrez une phrase: ")
ct = input("Entrez le caractère à compter: ")
print("Occurrence du caractère:", occurrence(pt, ct))
