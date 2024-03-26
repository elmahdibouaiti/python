def conv(temperature, n):
    # Check if n is 1 to convert from Celsius to Fahrenheit
    if n == 1:
        return temperature * 9/5 + 32
    # Check if n is 2 to convert from Fahrenheit to Celsius
    elif n == 2:
        return (temperature - 32) * 5/9
    else:
        return "n doit être égal à 1 pour convertir de Celsius à Fahrenheit ou égal à 2 pour convertir de Fahrenheit à Celsius."

temp = int(input("Entrez temperatur : "))
n = int(input("Entrez un entier (1 pour C à F, 2 pour F à C) : "))
print(conv(temp, n))
