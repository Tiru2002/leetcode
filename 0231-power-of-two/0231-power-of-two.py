import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        #return math.sqrt(n)==int(math.sqrt(n))
        #return math.floor(math.log2(n))==math.ceil(math.log2(n))
        return n&(n-1)==0