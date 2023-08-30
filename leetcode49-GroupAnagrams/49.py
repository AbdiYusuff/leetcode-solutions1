class Solution:
    strs = ["eat","tea","tan","ate","nat","bat"]
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs: 
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h: 
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
    print(groupAnagrams)
    