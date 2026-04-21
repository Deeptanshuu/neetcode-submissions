class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if str.isalnum(i):
                clean += i.lower()
                
        rev_cleaned = clean[::-1]
        
        if rev_cleaned == clean: 
            return True
        else: 
            return False
            