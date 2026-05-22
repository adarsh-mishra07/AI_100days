#right triangle
row =int(input("enter the of rows :"))

for i in range(1,row+1):
   print("*"*i)


#inverted Triangle Pattern 

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print("*" * i)

#pyramid Pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
