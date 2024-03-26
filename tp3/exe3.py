def voyelles(phrase):
    count = 0
    for char in phrase:
        if char.lower() in 'aeiouy':
            count += 1
    print("Le nombre de voyelles est :", count)


phrase = input("Entrez une phrase: ")
voyelles(phrase)
