class Solution:
    def reverse(self,n: int) -> int:
       #Defining 32 bit interger range
       MIN_int,MAX_int=-2**31,2**31-1
       #Checking the sign
       sign=(-1 if n<0 else 1)
       #Reversing the digits using string manipulation and adding the sign as checked before
       rev=(int(str(abs(n))[::-1]))*sign
       #Returing value if reverssed interger falles between the the 32 bit interger range otherwise return 0
       return (rev if MIN_int<=rev<=MAX_int else 0)