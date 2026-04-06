class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_words = defaultdict(list)


        offset = ord('a')


        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - offset] += 1
            
            
            freq_words["".join(str(freq))].append(word)

        print(freq_words.values())

        return list(freq_words.values())