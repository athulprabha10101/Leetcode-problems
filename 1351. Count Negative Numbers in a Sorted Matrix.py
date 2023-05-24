"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

"""


def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        for j in grid[i]:
            if j < 0:
                count += 1
    return count


# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#
#         #BINARY SEARCH
#         negative=0 #total negatives
#         for i in grid: #traverse every row of grid
#             l=0 #initial index of row
#             h=len(i)-1 #last index of that row
#             while l<=h: #traverse all indeces of any row
#                 mid=(l+h)//2 #middle index
#                 if i[mid]>=0: #if element is positive then no negative count
#                     l=mid+1 #then check ->negative may be present after mid element
#                 else:
#                     #negative count-> from the element found negative,after that index
#                     #every element present in non-increasing sorted row will have negatives
#                     negative+=h-mid+1
#                     h=mid-1 #then check if negatives present before that mid element
#         return negative