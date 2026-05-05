class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def is_valid(i):
            if i == len(nums):
                return True
            return False
        def get_candidates(i):
            
            return [[], nums[i]]

        def search(i, subset):
            if is_valid(i):
                res.append(subset.copy())
                return

            for candidate in get_candidates(i):
                if candidate != []:
                    subset.append(candidate)
                search(i + 1, subset)
            if subset:
                subset.pop()
        search(0, [])
        return res
            