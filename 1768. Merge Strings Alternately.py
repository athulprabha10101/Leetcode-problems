'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
'''




def mergeAlternately(word1 , word2):
    n1, n2 = len(word1), len(word2)
    result = ""

    i = 0

    while i < n1 and i < n2:
        result += word1[i]
        result += word2[i]
        i += 1
    while i < n1:
        result += word1[i]
        i += 1
    while i < n2:
        result += word2[i]
        i += 1
    return result

'''alternatively

n1, n2 = len(word1), len(word2)
        result = ""

        i = 0
        
        while i < n1 or i < n2:
            if i < n1:
                result += word1[i]
            if i < n2:    
                result += word2[i]
            i +=1
        return result
        
        '''

