class Personne:
    def __init__(self, nom, prenom, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Personne: {self.nom} {self.prenom}, Tel: {self.telephone}, Email: {self.email}"

class Travailleur(Personne):
    def __init__(self, nom, prenom, telephone, email, entreprise, adresse, tel_travail):
        super().__init__(nom, prenom, telephone, email)
        self.entreprise = entreprise
        self.adresse = adresse
        self.tel_travail = tel_travail

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Entreprise: {self.entreprise}, Adresse: {self.adresse}, Tel travail: {self.tel_travail}"

class Scientifique(Travailleur):
    def __init__(self, nom, prenom, telephone, email, entreprise, adresse, tel_travail, discipline, types):
        super().__init__(nom, prenom, telephone, email, entreprise, adresse, tel_travail)
        self.discipline = discipline
        self.types = types.split(',')  # Split string input into list of types

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Discipline: {self.discipline}, Types: {', '.join(self.types)}"

def create_personne():
    print("Enter details for Personne:")
    nom = input("Nom: ")
    prenom = input("Prenom: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    return Personne(nom, prenom, telephone, email)

def create_travailleur():
    print("Enter details for Travailleur:")
    nom = input("Nom: ")
    prenom = input("Prenom: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    entreprise = input("Entreprise: ")
    adresse = input("Adresse: ")
    tel_travail = input("Telephone Travail: ")
    return Travailleur(nom, prenom, telephone, email, entreprise, adresse, tel_travail)

def create_scientifique():
    print("Enter details for Scientifique:")
    nom = input("Nom: ")
    prenom = input("Prenom: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    entreprise = input("Entreprise: ")
    adresse = input("Adresse: ")
    tel_travail = input("Telephone Travail: ")
    discipline = input("Discipline: ")
    types = input("Types (comma-separated, e.g., Experimental,Theoretical): ")
    return Scientifique(nom, prenom, telephone, email, entreprise, adresse, tel_travail, discipline, types)

# Example of how you might use these functions:
person = create_personne()
print(person)
worker = create_travailleur()
print(worker)
scientist = create_scientifique()
print(scientist)
