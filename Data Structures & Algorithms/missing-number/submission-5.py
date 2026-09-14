class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity O(n^2)
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
        # return len(nums)


        # Time Complexity O(nlogn)
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # Time complexity O(n), memory O(1)
        # return sum(range(len(nums)+1)) - sum(nums)

        # Time complexity O(n), memory O(1)
        res = 0
        for i in range(len(nums)):
            res = res^i^nums[i]
        return res^len(nums)