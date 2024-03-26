def int__into__roman(num):
    """Converts an integer to a Roman numeral."""
    vals = [1000, 900, 500, 400, 100, 90, 50,  40, 10, 9, 5, 4, 1]
    nums = ["M", "CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman_numeral = ""
    i = 0	
    while  num > 0:
        
        if vals[i] <= num:
            roman_numeral += nums[i]
            num -= vals[i]
        else:
            i += 1
    return roman_numeral    

a = int(input("Enter a positive integer:"))
print(int__into__roman(a))