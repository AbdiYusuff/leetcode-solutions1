Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]     
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Solution and Explanation:
First sort the strings, which re-arranges the characters in alphabetically ascending order. All anagrams will now have the exact same arrangments of characters. From there, we can check if the sorted word exists in the hashmap  
1. Create a hashmap in which the 'key' would be the character and the "value" would be the character frequency. 
2. Iterate through strings in the given array and build the hashmaps.
3. Iterate through the newly created hashmaps to check if each key and the frequencies are equal. 
4. For each keys and frequences that are equal, add to a new array. 
5. Return array containing the arrays



