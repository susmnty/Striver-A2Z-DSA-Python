class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into words using split()
        words = s.strip().split()
        
        # Step 2: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 3: Join them back into a single string with single space
        return ' '.join(reversed_words)
