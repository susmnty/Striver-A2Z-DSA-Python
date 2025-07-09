from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        This function performs a binary search on a sorted list to find the index of a target value.
        If the target is not found, it returns -1.
        
        :param nums: List[int] - A list of integers sorted in ascending order.
        :param target: int - The integer value to search for in the list.
        :return: int - The index of the target in the list or -1 if not found.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1