#1 reverse a string
"""
def Reverse_Str(s):
 a=list(s)
 end=len(a)-1
 start=0

 while start<end:
  a[start], a[end] = a[end], a[start]
  end-=1
  start+=1
 return "".join(a)

reversed_str=input("Enter the string")
print("This is the reverse of String:", Reverse_Str(reversed_str))

"""

#2 pallindrom check 

"""
def pal(a):
 char=list(a)
 start=0
 end=len(char)-1
 while start<end:
  if char[start]==char[end]:
   start+=1
   end-=1
  else:
   return -1
 return 1

str=input("Enter the String")

if pal(str):
 print("Pallindrome String")
else:
 print("It is not palindrome")


""" 

#3 count of vowels and consonants in a string

"""

def vowCon(s):
 countVow=0
 countCon=0
 vowels="aeiouAEIOU"
 vow=''
 con=''
 for i in s:
  if ('A'<= i <='Z') or ('a'<= i <='z'):
   if i in vowels:
    vow+=i
    countVow+=1
   else:
    con+=i
    countCon+=1
 return countVow,vow,countCon,con



str=input("Enter the String")
countVow,vow,countCon,con = vowCon(str)

print("Vowels:", countVow, "→", vow)
print("Consonants:", countCon, "→", con)

"""

# tc=o(n^2) sc=o(n)


#“Using string concatenation leads to O(n²), so we optimize using lists to achieve O(n).”
"""

def vowCon(s):
    countVow = 0
    countCon = 0
    vowels = "aeiouAEIOU"
    
    vow_list = []
    con_list = []

    for ch in s:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            if ch in vowels:
                countVow += 1
                vow_list.append(ch)
            else:
                countCon += 1
                con_list.append(ch)

    return countVow, "".join(vow_list), countCon, "".join(con_list)

str=input("Enter the String")
countVow,vow,countCon,con = vowCon(str)

print("Vowels:", countVow, "→", vow)
print("Consonants:", countCon, "→", con)

"""

#4 remove space 
"""
def Remove_Space(s):
    result=""
    for ch in s:
        if ch !=' ':
          result+=ch
    return result
sen="Adarsh is good boy"
result=Remove_Space(sen)
print("String after removing spaces:", result)

#tc=o(n^2) sc=o(n)
"""
#Optimized Version (Interview Level)

"""
def Remove_Space(s):
    result=[]
    for ch in s:
        if ch !=' ':
          result.append(ch)
    return "".join(result)
sen="Adarsh is good boy"
result=Remove_Space(sen)
print("String after removing spaces:", result)

#tc=o(n) sc=o(n)
"""


#5  lower case to upper case

"""
def LotoUp(s):
    Upr=[]
    for ch in s:
        if 'a'<=ch<='z':
            a=ord(ch)-32
            Upr.append(chr(a))
        else:
            Upr.append(ch)
    return "".join(Upr)

str=input("Enter the String")
print("String after converting to uppercase:", LotoUp(str))

"""


#6 Count frequency of characters (hashing)

"""
def  char_freq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq


str=input("Enter the String")
frequency=char_freq(str)
print("Character Frequency:")
for ch, count in frequency.items():
    print(f"{ch}: {count} ")

"""

#7 Find first non-repeating character

"""
def NonRep(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    
    for ch in s:
        if freq[ch]==1:
            return ch
    return None

str=input("Enter the String")
result=NonRep(str)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")


    """

#8 Check anagram
"""
def Anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1={}
    for ch in s1:
        if ch in count1:
            count1[ch]+=1
        else:
            count1[ch]=1
    for ch in s2:
        if ch in count1:
            count1[ch]-=1
        else:
            return False
    for count in count1.values():
        if count != 0:
            return False
    return True

str1=input("Enter the first String")
str2=input("Enter the second String")
if Anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


"""

# 9. Remove duplicates from string
"""
s=input("Enter the String")
def Remove_Dup(s):
    seen={}
    result=[]
    for ch in s:
        if ch in seen:
            continue
        seen[ch]=True
        result.append(ch)
    return "".join(result)

print("String after removing duplicates:", Remove_Dup(s))

"""

#10 find length with len()

str=input("Enter the String")
def length(s):
    count=0
    for ch in str:
        count+=1
    return count

print("Length of the string:",length(str))











