class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum

            if sum == 1:
                return True
            if sum in visited:
                return False
            visited.add(sum)






