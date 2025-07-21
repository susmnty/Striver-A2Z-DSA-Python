class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            current_load = 0
            required_days = 1  # Start with first day
            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = 0
                current_load += weight
            return required_days <= days

        left = max(weights)         # At least the max weight
        right = sum(weights)        # At most all weights in one day

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left
