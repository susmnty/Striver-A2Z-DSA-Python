class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        def power(x, n):
            res = 1
            for _ in range(n):
                res *= x
                if res > m:
                    return res  # early exit
            return res

        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2
            mid_pow = power(mid, n)

            if mid_pow == m:
                return mid
            elif mid_pow < m:
                low = mid + 1
            else:
                high = mid - 1

        return -1
