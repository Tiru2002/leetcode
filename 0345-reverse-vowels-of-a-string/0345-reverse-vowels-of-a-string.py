class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        word=list(s)
        v=['a','e','i','o','u','A','E','I','O','U']
        while(l<r):
            while l<r and word[l] not in v:
                l+=1
            while l<r and word[r] not in v:
                r-=1
            word[l],word[r]=word[r],word[l]
            l+=1
            r-=1
        return "".join(word)
        