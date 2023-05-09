"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.



Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

"""


def findLucky(arr):
    n = len(arr)
    largest = float('-inf')
    for i in range(n):
        count = 1
        for j in range(n):
            if arr[i] == arr[j] and i != j:
                count += 1

        if count == arr[i] and arr[i] > largest:
            largest = arr[i]

    if largest != float('-inf'):
        return largest
    else:
        return -1

print(findLucky([1,2,2,3,4]))