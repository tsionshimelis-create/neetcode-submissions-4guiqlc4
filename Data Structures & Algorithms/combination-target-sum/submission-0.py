class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def is_valid(state):
            if sum(state) == target:
                return True
            return False
        
        def get_candidates(i):
            return nums[i:]
        
        def search(state, start):
            nonlocal res
            if is_valid(state):
                res.append(state.copy())
                return 
            if sum(state) > target:
                return False
            
            for i in range(start, len(nums)):
                state.append(nums[i])
                search(state, i)
                state.pop()
        search([], 0) 
        return res
            

        