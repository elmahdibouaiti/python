def multipleDe3():
    multiples = [] 
    for i in range(1, 1001): 
        if i % 3 == 0:  
            multiples.append(i)  
    return multiples


print("Multiples de 3 entre 1 et 1000:", multipleDe3())
