# Process the string:
# - convert to lowercase
# - remove the nonalphanumeric characters
# - remove the spaces
# - append characters into a new string
# Check if reversed string == string

def isPalindrome(s):
    s = s.lower()
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s = new_s+char
    new_ss = ''.join(reversed(new_s))
    print(new_ss)
    print(new_s)
    if new_ss == new_s:
        return True
    else:
        return False 
    
s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)
        
   

