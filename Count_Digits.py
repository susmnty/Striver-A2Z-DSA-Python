#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        temp = n
        
        while temp > 0:
            digit = temp%10
            if digit != 0 and n % digit == 0:
                count += 1
            temp //= 10
            
        return count