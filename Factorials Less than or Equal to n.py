#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here
     res = []
     fact = 1
     i = 1
     
     while fact <= n:
         res.append(fact)
         i += 1
         fact *= i
         
     return res  