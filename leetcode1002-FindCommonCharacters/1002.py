def commonChars(words):
    # l = []
    # for i in words[0]:
    #     for j in range(len(words)):
    #         if i in words[j]:
    #             temp = words[j]
    #             words[j] = temp.replace(i,"", 1) 
    #             print(words[j])
    #         else:
    #             break
    #         if j == len(words)-1:
    #             l.append(i)
    # return l

    # Initialize a dictionary to store character counts from the first word
    common_char_counts = {}
    
    # Count characters in the first word
    for char in words[0]:
        common_char_counts[char] = common_char_counts.get(char, 0) + 1
        # print(common_char_counts)
    
    # Iterate through the rest of the words
    for word in words[1:]:
        # Create a dictionary to store character counts for the current word
        word_char_counts = {}
   
        
        # Count characters in the current word
        for char in word:
            word_char_counts[char] = word_char_counts.get(char, 0) + 1
            print(word_char_counts)
        
        # Update common_char_counts to contain the minimum counts
        for char in common_char_counts:
            if char in word_char_counts:
                common_char_counts[char] = min(common_char_counts[char], word_char_counts[char])
            else:
                # If the character is not present in the current word, remove it from common_char_counts
                common_char_counts[char] = 0
    
    # Convert character counts to a list of characters
    result = []
    for char, count in common_char_counts.items():
        result.extend([char] * count)
    
    return result
words = ["bella","label","roller"]
res = commonChars(words)
print(res)
