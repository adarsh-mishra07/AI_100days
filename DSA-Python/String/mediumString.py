# 11 .Longest substring without repeating characters ⭐

'''
def Longest_Substring(s):
    left,max_length=0,0
    track=set()
    for right in range(len(s)):
      while s[right] in track:
        track.remove(s[left])
        left+=1
      
      track.add(s[right])
      max_length=max(max_length,right-left+1)
    return max_length      
s=input("Enter the String")
print("Length of the longest substring without repeating characters:", Longest_Substring(s))

'''

#12 String compression (aaabb → a3b2)
'''
def String_Compression(s):
    if s=='':
        return ''
    result=''
    count=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            result+=s[i]+str(count)
            count=1
    result+=s[-1]+str(count)  #for the last character , we use like that because the loop will end before processing the last character
    return result

s=input("Enter the String")
print("Compressed String:", String_Compression(s))

'''

#13 Check valid parentheses
'''
def isValid(s):
    stack=[]
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack:
                return False
            top=stack.pop()
            if (ch==')' and top!='(') or (ch=='}' and top!='{') or (ch==']' and top!='['):
                return False
    return len(stack)==0

s=input("Enter the String")
if isValid(s):
    print("The parentheses are valid.")
else:    print("The parentheses are not valid.")

'''

#14 Check if one string is rotation of another
'''
def IsRotation(s1,s2):
    temp=''
    if len(s1) != len(s2):
        return False
    temp=s1+s1
    if s2 in temp:
        return True
    else:
        return False
s1=input("Enter the first String")
s2=input("Enter the second String")
if IsRotation(s1,s2):
    print("The strings are rotations of each other.")
else:    print("The strings are not rotations of each other.")

'''

#15 Reverse words in a sentence

'''
def reverse_words(s):
    words=''
    wordList=[]

    for ch in s:
        if ch !=' ':
            words+=ch
        else:
            if words !=' ':
                wordList.append(words)
                words=''
    #adding the last word to the list
    if words !='':
        wordList.append(words)

    #reversing the list of words
    reverse_s=' '
    for i in range(len(wordList)-1,-1,-1):
        reverse_s+=wordList[i]
        if i!=0:
            reverse_s+=' '
    return reverse_s
    

s=input("INput the string")
print("Reverse words in setnence:", reverse_words(s))

'''

# reverse everything in the string (e.g., "hello world" → "dlrow olleh")

'''
def reverse_everything(s):
    result = ""
    # String ki length nikaalein
    length = 0
    for char in s:
        length += 1
        
    # Piche se loop chalayein (n-1 se 0 tak)
    for i in range(length - 1, -1, -1):
        result += s[i]
        
    return result

# Test
s = input("Input the string: ")
print("Everything reversed:", reverse_everything(s))


'''

#16 count the words in a string

def count_words(s):
    count=0
    in_word=False
    for ch in s:
        if ch!=' ':
            if not in_word:
                count+=1
                in_word=True
        else:           
            in_word=False
    return count

s=input("Input the string: ")
print("Number of words in the string:", count_words(s))