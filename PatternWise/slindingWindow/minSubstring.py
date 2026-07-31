from collections import Counter            #it returns dictionary
def solution(s,t):
   if not s or not t or len(s)<len(t):      
     return ""
   dict_t=Counter(t)
   require= len(dict_t)

   l,r=0,0
   window_counts={}
   formed=0
   ans=float("inf"),None,None     # result,l,r

   while r<len(s):
     ch=s[r]
     window_counts[ch]=window_counts.get(ch,0)+1
     
     if ch in dict_t and window_counts[ch]==dict_t[ch]:
        formed+=1
     while l<=r and formed==require:
        ch=s[l]
        
        if r-l+1 < ans[0]:
               ans=(r-l+1,l,r)
        
        window_counts[ch]-=1
        
        if ch in dict_t and window_counts[ch]<dict_t[ch]:
           formed-=1
        l+=1
     r+=1
   return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
   


print(solution("ADOBECODEBANC","ABC"))
