class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        pairs = {")":"(", "}":"{", "]":"["}

        for i in range(len(s)):
            if s[i] in pairs:
                if stack and stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(s[i])
        if stack:
            return False
        return True