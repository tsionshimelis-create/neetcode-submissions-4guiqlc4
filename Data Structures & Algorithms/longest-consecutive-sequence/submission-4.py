class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

# [2, 3, 4, 4, 5, 10, 20]
        res = 0
# [0, 1, 1, 2, 3, 4, 5, 6]
        curr = nums[0]
        streak = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                streak += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = max(streak, res)
                streak = 1
        return  max(streak, res)

        

