class Solution:

    def encode(self, strs: List[str]) -> str:
        parts =  []
        for s in strs:
            parts.append(str(len(s)).zfill(3) + s)
        return ''.join(parts)
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            l = int(s[i:i+3])
            i += 3
            result.append(s[i:i+l])
            i += l
        return result