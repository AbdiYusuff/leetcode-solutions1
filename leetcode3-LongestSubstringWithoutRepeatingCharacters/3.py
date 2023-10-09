def longestUniqueSubstring(s):
    start, longest = 0, 0
    chars = {}
    for i in range(len(s)):
        if s[i] in chars and chars[s[i]] >= start:
                start = chars[s[i]] + 1
                print(chars)
        longest = max(longest, i - start + 1)
        chars[s[i]] = i
        print(start)     
    return longest
    
s = "abcdeabc"
print(s)
result = longestUniqueSubstring(s)
print(result)
