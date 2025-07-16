class solution:
    def floorsqrt (self, n):
        if n == 0 or n ==1:
            return n
        
        start = 1
        end = n
        ans = 0
        
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                return mid + 1
            else:
                end = end - 1
                
        return ans