class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            key="".join(sorted(s))
            if key not in dic:
                dic[key]=[]
            dic[key].append(s)
        return list(dic.values())