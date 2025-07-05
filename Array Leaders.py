class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        
        max_from_right = arr[-1]
        leaders_list.append(max_from_right)

        # Traverse from second last to the beginning
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders_list.append(arr[i])
        
        # We collected leaders from right to left → reverse it
        leaders_list.reverse()
        return leaders_list