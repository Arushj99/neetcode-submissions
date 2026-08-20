class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            num = i
            
            while s[num] != "#":
                num += 1
            length = int(s[i: num])
            res.append(s[num + 1: num + 1 + length])
            i = num + 1 + length

        return res