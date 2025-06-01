# Decision Making in Java

class Solution:
    def compareNM(self, n: int, m: int) -> str:
        if n > m:
            return "greater"
        elif n < m:
            return "lesser"
        else:
            return "equal"