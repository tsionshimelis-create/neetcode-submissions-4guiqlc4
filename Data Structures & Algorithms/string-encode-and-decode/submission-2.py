class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for phrase in strs:
            encoded_string += phrase + "ድ"
        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string = []

        decoded_string.extend(s.split("ድ"))

        return decoded_string[:-1]