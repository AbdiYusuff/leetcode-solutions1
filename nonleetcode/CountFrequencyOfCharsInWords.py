#Given an array of words, 
#Count the frequency of all chars
#using hash sets

def charFrequencyCounter(words):
    word_char_count = {}
    for word in words:
        for char in word:
            word_char_count[char] = word_char_count.get(char,0)+1
    return max(word_char_count.values())
words = ["bella","label","roller"]
result = charFrequencyCounter(words)
print(result)
