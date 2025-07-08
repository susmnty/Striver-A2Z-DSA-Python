class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 
        prefix_sum = 0 
        prefix_map = {0:1}

        for nums in nums:
            prefix_sum += nums
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count