class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        m = len(arr[0])
        
        max_row = -1
        j = m - 1
        
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                max_row = i
                
        return max_row