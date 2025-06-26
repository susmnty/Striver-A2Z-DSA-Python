#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here
        n = len(a)
        m = len(b)
        i = j = 0
        union = []

        while i < n and j < m:
            # Skip duplicates in a
            while i > 0 and i < n and a[i] == a[i-1]:
                i += 1
            # Skip duplicates in b
            while j > 0 and j < m and b[j] == b[j-1]:
                j += 1
            
            if i < n and j < m:
                if a[i] < b[j]:
                    union.append(a[i])
                    i += 1
                elif a[i] > b[j]:
                    union.append(b[j])
                    j += 1
                else:
                    union.append(a[i])
                    i += 1
                    j += 1

        # Remaining elements in a
        while i < n:
            if i == 0 or a[i] != a[i-1]:
                union.append(a[i])
            i += 1

        # Remaining elements in b
        while j < m:
            if j == 0 or b[j] != b[j-1]:
                union.append(b[j])
            j += 1

        return union