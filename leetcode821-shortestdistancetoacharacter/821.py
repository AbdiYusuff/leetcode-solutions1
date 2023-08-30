print('before function starts')
TestString = 'loveisintheair'
Charac = 'i'
def shortestToChar(s: str, c: str) -> list[int]:
        # occurence of charachter in the array.
        print('Now the function starts')
        occ = []
        for i in range(len(s)):
            if s[i] == c:
                occ.append(i)
                print('inside forloop here')
        ans = []
        for i in range(len(s)):
            #checking distance of each point from occurences ans the selecting the least distance. 
            tmplst = []
            for j in occ:
                tmplst.append(abs(i-j))
            ans.append(min(tmplst))
       
        
        return ans
        

out = shortestToChar(TestString,Charac)
print('printing output after function call')
print(out)   
    