class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sett_nums = set(nums)
        res = 0

        for num in nums:
            curr = num
            streak = 0
            while curr in sett_nums:
                streak += 1
                curr += 1
            res = max(res, streak)

        return res

