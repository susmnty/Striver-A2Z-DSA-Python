class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are not palindromes
        if x < 0:
            return False

        # convert number to string 
        x_str = str(x)

        #Compare with its reverse
        return x_str == x_str[::-1]