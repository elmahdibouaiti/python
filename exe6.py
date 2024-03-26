
moyenne = float(input("Entrez votre moyenne : "))
if moyenne >= 16:
    mention = "Très bien"
elif moyenne >= 14:
    mention = "Bien"
elif moyenne >= 12:
    mention = "Assez bien"
elif moyenne >= 10: 
    mention = "Passable"
else:
    mention = "Insuffisant"
    
print("Votre mention est :", mention)
