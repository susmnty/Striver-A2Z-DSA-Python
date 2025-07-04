class Solution:
    def maxSum(self, arr):
        max_pair_sum = float('-inf')  # Initialize with a very small value

        for i in range(len(arr) - 1):
            pair_sum = arr[i] + arr[i + 1]
            max_pair_sum = max(max_pair_sum, pair_sum)

        return max_pair_sum
