class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def is_valid(total):
            if total == target:
                return True
        
        def search(state, start, total):
            if is_valid(total):
                res.append(state.copy())
                return
            if sum(state) > target:
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                state.append(candidates[i])
                search(state, i + 1, total + candidates[i])
                state.pop()

        search([], 0, 0)
        return res
