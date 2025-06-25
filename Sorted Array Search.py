#User function Template for python3

class Solution:
    def searchInSorted(self, arr, k):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                return 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return 0  # Use 0 instead of -1 to make print("true" if ...) behave correctly
