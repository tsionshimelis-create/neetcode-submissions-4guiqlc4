class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = defaultdict(int)
        length = 0
        l = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
            
        return length
