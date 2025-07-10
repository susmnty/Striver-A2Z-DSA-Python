class Solution:
    def countFreq(self, arr, target):
        def first_occurrence():
            low, high = 0, len(arr) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    first = mid
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def last_occurrence():
            low, high = 0, len(arr) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    last = mid
                    low = mid + 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        first = first_occurrence()
        last = last_occurrence()

        if first == -1:
            return 0
        return last - first + 1
