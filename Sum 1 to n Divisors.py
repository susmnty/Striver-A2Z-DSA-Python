class Solution:
    def sumOfDivisors(self, n):
    #code here 
    total = 0
    for i in range (1, n + 1):
        total += (n // i) * i
    return total