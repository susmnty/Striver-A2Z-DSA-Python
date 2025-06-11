class Solution:
    def selectionsort(self, arr):
        for i in range(len(arr)):
            min_idx = i 
            for i in range(len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j 
            arr[i], arr[min_idx] = arr[min_idx], arr[i]