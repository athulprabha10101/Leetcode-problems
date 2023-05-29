"""
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.


Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
"""



def minNumber(nums1, nums2):

    n = 10
    for i in nums1:
        if i in nums2:
            n = min(n, i)
    if n != 10:
        return n

    x = min(nums1)
    y = min(nums2)
    a = x * 10 + y
    b = y * 10 + x
    return min(a, b)