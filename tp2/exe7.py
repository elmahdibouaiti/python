cmp = 0
mt_c = "1234"
mt_s = input("Veuillez entrer votre mot de passe : ")

while cmp < 3 and mt_s != mt_c:
   print("Mot de passe incorrect.")
   mt_s = input("Veuillez entrer votre mot de passe : ")
   cmp += 1

if cmp == 3:
   print("Carte bancaire retenue.")
else:
    print("welcome")