def findTheDifference(s, t):
    if len(s) > len(t):
        com = s
        diff = ""
        for i in t:
            if i in com and com.count(i) > 0:
                pass
            else:
                diff+=i
                
    else:
        com = t
        for i in s:
            if i in com and com.count(i) > 0:
                pass
            else:
                diff+=i 
    return f"diff"
    
    
s="aaa"
t="aa"
findTheDifference(s,t)