#Assignment question -1
#List me 10 numbers lo → max, min, sum, average print karo

list=[1,2,3,4,5,6,7,8]
print("Maximum=",max(list),", mini=",min(list),",sum=",sum(list))

#Assignment question - 2
#Dictionary me 5 students ke marks store karo → topper find karo

Student_marks={"Adarsh":10,"virat":9,"Sun":8,"Moon":7,"Earth":6}
topper=max(Student_marks,key=Student_marks.get)
print(f"Topper:{topper} with {Student_marks[topper]} marks")

#Assignment Question -3
#Set me do sets ka union, intersection, difference nikalo

set1={1,2,3,4}
set2={1,2,5,6}

union_result=set1.union(set2)
print(union_result)

intersection_result=set1.intersection(set2)
print(intersection_result)

diff_result=set1.difference(set2)
print(diff_result)

#Assignment ques- 4
#Tuple me 5 values store karo → index & slicing apply karo

tuple1=(10,20,30,40)
print("Index 0:",tuple[0])
print("Index 1:",tuple[1])  #index: Specific position of elemtn

print("Slice [1:4]",tuple1[1:4])
print("Slice [:3]",tuple1[:4])
print("Slice [2:]",tuple1[2:])