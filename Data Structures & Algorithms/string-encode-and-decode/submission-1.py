class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)).zfill(3) + s
        return result
    
    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            l = int(s[:3])
            result.append(s[3:l + 3])
            s = s[3 + l:]
        return result