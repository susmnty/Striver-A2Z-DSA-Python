class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        current = 1
        i = 0
        
        while k > 0:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return current
            current += 1
