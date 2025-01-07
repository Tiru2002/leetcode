class Solution:
    def addDigits(self, num: int) -> int:
        l=list(map(int,str(num)))

        if len(l)==1:
            return l[0]
        while len(l)>1:
            s=sum(l)
            l=list(map(int,str(s)))
        return s






        