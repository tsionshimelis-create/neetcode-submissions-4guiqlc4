class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,2,3,2,2]
        # [0,1,2,3,4]
        # 1 => 2 => 3 
        #      2 <= 3
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow

