# 1..list sum and average

number=[1,2,3,4]
print("Sum:",sum(number))
print("Average:",sum(number)/len(number))

# 2.. Dictionary Based login System

users={"adarsh":"1234","virat":"8815823607"}
user=input("username:")
pwd=input("password")

if user in users and users[user]==pwd:
    print("Login Successful")

else:
    print("Invalid Credentials")


# 3 Even number using list

nums=[1,2,3,4,5,6]
even=[]

for n in nums:
    if(n%2==0):
        print(n)

#4 . tuple unpacking 

a,b,c=(10,20,30)
print(a,b,c)