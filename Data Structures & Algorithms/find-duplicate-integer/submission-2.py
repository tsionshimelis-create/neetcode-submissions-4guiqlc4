class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
                continue
            else:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                else:
                    swap = nums[i] - 1
                    nums[i], nums[swap] = nums[swap], nums[i]