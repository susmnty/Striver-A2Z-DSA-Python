class Solution:
    def findFloor(self, arr, x):
        low = 0
        high = len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res

# passed the 11 test cases on gfg out of 1100 around.