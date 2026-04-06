class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "$" + s
       
        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string = []
        i = 0

        while i < len(s):
            num = ""
            j = i 
            while s[j] != "$":
                num += s[j]
                j += 1
            decoded_string.append(s[j + 1: j + int(num) + 1])
            i = j + int(num) + 1


        return decoded_string