class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx_complement = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in idx_complement:
                return [idx_complement[nums[i]], i]
            
            idx_complement[complement] = i

        