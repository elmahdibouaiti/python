# PYTHON PART-0

**Introduction**

This repository contains the code from simple to mid exercises in Python. The exercises cover basic mathematical operations, conditional statements, and loops.

## Summary

### Exercise 1: Printing Variables**
### Exercise 2: Addition and Multiplication**
### Exercise 3: Division**
### Exercise 4: Sorting Integers**
### Exercice 5 Quadratic Equation Solver in Python**


## Exercise 1: Printing Variables**

The first exercise simply prints the values of two variables, `a` and `b`.

```python
a, b = 12, 16.5
print("a = ", a)
print("b = ", b)
```

## Exercise 2: Addition and Multiplication**

The second exercise prompts the user to enter two numbers, then calculates and prints their sum and product.

```python
nb1 = int(input("Entrer le premier nombre"))
nb2 = int(input("Entrer le deuxieme nombre"))

s = nb1 + nb2
m = nb1 * nb2

print("Somme : ", s)
print("multiplication : ", m)
```

## Exercise 3: Division**

The third exercise prompts the user to enter two numbers, then calculates and prints their quotient and remainder. If the second number is 0, it prints an error message.

```python
nb1 = int(input("Entrer le premier nombre"))
nb2 = int(input("Entrer le deuxieme nombre"))

if nb2 == 0:
    print("Impossible de diviser par zero")
else:
    q = nb1 // nb2
    r = nb1 % nb2
    print("Le quotient est", q, "et le reste est", r)
```

## Exercise 4: Sorting Integers**

The fourth exercise prompts the user to enter three integers, then sorts them in ascending order and prints them.

```python
x = int(input("Entrez le premier entier: "))
y = int(input("Entrez le deuxième entier: "))
z = int(input("Entrez le troisième entier: "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("Les entiers classés par ordre croissant sont:", x, y, z)
```

## Exercice 5 Quadratic Equation Solver in Python**

**Introduction:**
This Python script is designed to solve quadratic equations of the form `ax^2 + bx + c = 0`, where `a`, `b`, and `c` are real numbers and `x` is the unknown variable. The code employs a step-by-step approach to determine the nature and solutions of the quadratic equation based on the discriminant, which is calculated using the formula `b^2 - 4ac`.

**Step-by-Step Explanation:**

1. **Importing the `math` Module:**
   ```python
   import math
   ```
   This line imports the `math` module, which provides various mathematical functions and constants. We will use the `math.sqrt()` function to calculate the square root of the discriminant.

2. **User Input:**
   ```python
   a = float(input("Entrez le coefficient a : "))
   b = float(input("Entrez le coefficient b : "))
   c = float(input("Entrez le coefficient c : "))
   ```
   These lines prompt the user to enter the coefficients `a`, `b`, and `c` of the quadratic equation. The `float()` function converts the user's input from a string to a floating-point number.

3. **Calculating the Discriminant:**
   ```python
   discriminant = b**2 - 4*a*c
   ```
   This line calculates the discriminant of the quadratic equation using the formula `b^2 - 4ac`. The discriminant determines the nature of the equation's solutions.

4. **Determining the Nature of Solutions:**
   - **If `discriminant > 0`:**
     ```python
     x1 = (-b + math.sqrt(discriminant)) / (2*a)
     x2 = (-b - math.sqrt(discriminant)) / (2*a)
     print("L'équation a deux solutions réelles sont :", x1, "et", x2)
     ```
     In this case, the discriminant is positive, indicating that the quadratic equation has two distinct real solutions. The code calculates these solutions using the quadratic formula and prints them to the console.

   - **If `discriminant == 0`:**
     ```python
     x = -b / (2*a)

**Conclusion**

These exercises provide a basic introduction to Python programming. They cover a variety of topics, from simple mathematical operations to conditional statements and loops. By working through these exercises, a junior

