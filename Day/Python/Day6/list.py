#create_list

listEle=[10,20,"Orange",5.8]
print(listEle)

#access
print(listEle[0])   #its forword
print(listEle[-1])  #its backword


#modify
listEle[2]="Grapes"
print(listEle)


#add/remove

listEle.pop()
print(listEle)

listEle.append("Append Element")
listEle.insert(1,20)
listEle.remove(10)
print(listEle)


#by loop 

for i in listEle:
    print("loop=",i)

