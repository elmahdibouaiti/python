def premiers(lf, ls):
    premiers = []
    for num in range(lf, ls + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                premiers.append(num)
    return premiers


lf = int(input("Entrez la limite inférieure: "))
ls = int(input("Entrez la limite supérieure: "))
print("Nombres premiers:", premiers(lf, ls))
