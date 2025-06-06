class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit 
            x = x // 10

        rev = rev * sign 

        #check if its 32 bit range
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev 