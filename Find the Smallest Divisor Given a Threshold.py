from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor):
            return sum(math.ceil(num / divisor) for num in nums)

        left, right = 1, max(nums)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if compute_sum(mid) <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer