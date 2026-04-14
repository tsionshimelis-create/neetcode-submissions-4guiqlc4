class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        length = 0
        l = 0
        offset = ord('A')
        for r in range(len(s)):
            count[ord(s[r]) - offset] += 1
            change = r - l + 1 - max(count)

            while change > k:
                count[ord(s[l]) - offset] -= 1
                l += 1
                change = r - l + 1 - max(count)
            length = max(length , r - l + 1)

        return length