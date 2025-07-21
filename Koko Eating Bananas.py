from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right  # Initialize with the max possible speed

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours <= h:
                result = mid
                right = mid - 1  # Try to minimize speed
            else:
                left = mid + 1  # Need to eat faster

        return result
