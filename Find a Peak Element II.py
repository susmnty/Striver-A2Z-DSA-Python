class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2

            max_row =  0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            curr = mat[max_row][mid]
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 <n else -1

            if curr > left_val and curr > right_val:
                return [max_row, mid]
            elif left_val > curr:
                right = mid - 1
            else:
                left = mid + 1
