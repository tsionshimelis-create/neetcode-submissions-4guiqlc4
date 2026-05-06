class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def is_valid(state):
            if sum(state) == target:
                return True
        
        def search(state, start):
            if is_valid(state):
                res.append(state.copy())
                return
            if sum(state) > target:
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                state.append(candidates[i])
                search(state, i + 1)
                state.pop()

        search([], 0)
        return res
