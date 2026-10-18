class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x<0:
            return False
        original,revers=x,0
        # Mathematically reverse the integer
        while x>0:
            r=x%10
            revers=(revers*10)+r
            x//=10
        # Return True if the reversed number matches the original
        return revers==original