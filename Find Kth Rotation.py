class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            # If array is already sorted
            if arr[low] <= arr[high]:
                return low
            
            mid = (low + high) // 2
            
            # Check if mid is the smallest
            if arr[mid] < arr[mid - 1]:
                return mid
            if arr[mid] > arr[mid + 1]:
                return mid + 1
            
            # Decide which half to go
            if arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
