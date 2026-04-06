class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = Counter(s)
        t = Counter(t)

        if len(t) != len(s):
            return False

        for key in s.keys():
            if s[key] != t[key]:
                return False

        return True
