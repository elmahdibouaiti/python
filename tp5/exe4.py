def creation_alphabet(clef):
    alphabet = ""
    for char in clef:
        if char.isalpha() and char.lower() not in alphabet:
            alphabet += char.lower()
    for char in range(97, 123):
        if chr(char) not in alphabet:
            alphabet += chr(char)
    return alphabet.upper()

def chiffrement(texte, clef):
    alphabet = creation_alphabet(clef)
    result = ""
    for char in texte:
        if char.isalpha():
            index = ord(char.lower()) - 97
            result += alphabet[index]
    return result


clef = 'CPBX%'
texte = 'CARTE'

alphabet_cree = creation_alphabet(clef)
texte_chiffre = chiffrement(texte, clef)

print("Alphabet créé:", alphabet_cree)
print("Texte chiffré:", texte_chiffre)
