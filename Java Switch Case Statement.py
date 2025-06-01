# Java Switch Case Statement
 # as coming to this question i have made mistake in this hardly 2 test cases pass.
 # overall with this logic i have understood and made, if any better solution do please note.
 
#User function Template for python3
class Solution:
    def switchCase(self, choice, arr):
        if len(arr) < 2:
            return 0

        a, b = arr[0], arr[1]

        if choice == 1:
            return a + b
        elif choice == 2:
            return a * b
        elif choice == 3:
            return a - b
        else:
            return 0