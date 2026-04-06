class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        count = Counter(nums)

        for value in count.values():
            if value >= 2:
                return True
        return False