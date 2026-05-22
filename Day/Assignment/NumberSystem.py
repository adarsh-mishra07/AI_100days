"""
Q1

Write a python script to print any number and its binary equivalent.

Q2

Write a python script to store binary number 1100101 in a variable and print it in decimal format.

Q3

Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.

Q4

Write a python script to store an octal number 125 in a variable and print it in binary format.

Q5

Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.

"""

#1 Write a python script to print any number and its binary equivalent.
"""
def decimal_to_binary(n):
    if n==0:
        return "0"
    
    binary_digits=[]

    while n>0:
        remainder=n%2
        binary_digits.append(str(remainder))
        n=n//2
    return "".join(binary_digits[::-1])

num=10
print(decimal_to_binary(num))

"""



#q2 - Write a python script to store binary number 1100101 in a variable and print it in decimal format.
"""
def bin_to_deci(n):
    deci=0
    power=0
    while n>0:
      digit=n%10
      deci=deci+digit*(2**power)
      n//=10
      power+=1
    return deci

print(bin_to_deci(1001))

"""

#q3
"""
Step 1: Hex → Decimal
Step 2: Decimal → Octal

"""
# Hex to Decimal
hex_num = "2F"

decimal = 0

# F = 15 manually
decimal = 2 * 16 + 15

# Decimal to Octal
n = decimal
octal = ""

while n > 0:
    rem = n % 8
    octal = str(rem) + octal
    n = n // 8

print(octal)


#q4
octal = 125

binary = ""

while octal > 0:
    digit = octal % 10

    if digit == 0: b = "000"
    elif digit == 1: b = "001"
    elif digit == 2: b = "010"
    elif digit == 3: b = "011"
    elif digit == 4: b = "100"
    elif digit == 5: b = "101"
    elif digit == 6: b = "110"
    elif digit == 7: b = "111"

    binary = b + binary
    octal //= 10

# remove leading zeros 
i = 0
while i < len(binary) and binary[i] == '0':
    i += 1

print(binary[i:])


#5

# Octal → Decimal
octal = 25
dec1 = 0
power = 0

while octal > 0:
    digit = octal % 10
    dec1 += digit * (8 ** power)
    octal //= 10
    power += 1

# Hex → Decimal
hex_num = "39"
dec2 = 0
power = 0

for i in range(len(hex_num)-1, -1, -1):
    digit = ord(hex_num[i]) - ord('0')
    dec2 += digit * (16 ** power)
    power += 1

# Add
total = dec1 + dec2

# Decimal → Binary
binary = ""

while total > 0:
    rem = total % 2
    binary = str(rem) + binary
    total //= 2

print(binary)