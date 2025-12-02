profile={
    "name":"adarsh",
"age":22,
"skill":["python","DSA"],
"city":"Delhi",
"is_code":True,
"project":["portfolio","AI project"]
}

print("\nInitial Profile")
print(profile)

#add new skill
new_skill=input("\nEnter a new skill to add")
profile["skill"].append(new_skill)

#update city
new_city=input("input your new city")
profile["city"]=new_city

#delete age
profile.pop("age")

#print all key value pairs
print("\nUpdated Profile Information")
for key,value in profile.items():
    print(f"{key}:{value}")