class Solution:
    def calculateMultiples(self, n):
        i = 10
        res = []
        while i >= 1:
            res.append(str(n * i))
            i -= 1
        print(" ".join(res))