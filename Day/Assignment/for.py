#1
a="Adarsh"
for i in a:
    print(f"Unicode of {i} :", ord(i))

#2 - to print whether the character is vowel or consonant
a="Adarsh" 
vowel="aeiouAEIOU"
for i in a:
    if i in vowel:
        print(f"{i} is a vowel")
    else:
        print(f"{i} is not a vowel")

#3 
sen="Adarsh is a good boy"
count =0
for i in sen:
    if i==' ':
        count+=1
print("Number of spaces in the sentence is:", count)

#4 unique digits in a integer
num=1234567890
num_str=str(num)
unique_digits=set(num_str)
print("Unique digits in the number are:", unique_digits)

#5 to count number of digits in a number
num=1234567
count=0
while num > 0:
    num //= 10
    count += 1
print("Number of digits in the number is:", count)
