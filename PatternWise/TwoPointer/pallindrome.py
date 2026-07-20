def Pal(a): 
    def check(str,end):
      while srt<end:
        if a[srt]!=a[end]:
            return False
        srt+=1
        end-=1
    return True

    length=len(a)
    srt=0
    end=length-1
    while srt<end:
       if a[srt]==a[end]:
              srt+=1
              end-=1
       else:
           return check(srt+1,end) or check(srt,end-1)
           
st =input("Enter the String:")
s=Pal(st)
print("The String is:",s)

