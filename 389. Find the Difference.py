class Solution:
    def findTheDifference(t,s):
        sumt, sums = 0, 0
        for i in t:
            sumt = sumt + ord(i)
        for i in s:
            sums = sums + ord(i)

        return chr(sumt - sums)