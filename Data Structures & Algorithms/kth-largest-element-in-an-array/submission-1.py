class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]

        heapq.heapify(nums)

        while k > 0:
            kthLargest = -heapq.heappop(nums)
            k -= 1

        return kthLargest