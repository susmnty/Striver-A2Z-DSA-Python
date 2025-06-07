#User function Template for python3

from typing import List
import math 

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        gcd = math.gcd(a,b)
        lcm = (a * b) // gcd
        return [lcm,gcd]