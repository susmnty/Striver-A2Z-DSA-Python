class Solution:
    def largest(self, arr):
        # code here
        max_element = arr[0]
        
        for num in arr:
            if num > max_element:
                max_element = num 
                
        return max_element