# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_index = {0: -1}
        cur_sum = 0
        best_len = 0
        
        for i, num in enumerate(arr):
            cur_sum += num
            
            if cur_sum not in prefix_index:
                prefix_index[cur_sum] = i
                
            target = cur_sum - k
            if target in prefix_index:
                best_len = max(best_len, i - prefix_index[target])
                
        return best_len