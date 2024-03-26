def IMC(p, t):
    imc = p / (t**2)
    if imc < 16:
        print("Anorexie ou dénutrition") 
    elif imc < 18.5:
        print("Maigreur") 
    elif imc < 25:
        print("Corpulence Normale") 
    elif imc < 30:
        print("Surpoids") 
    else:
        print("Obésité") 

p = float(input("Entrez votre poid en kg: "))
t = float(input("Entrez votre taille en mètres: "))
IMC(p, t)
