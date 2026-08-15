class Solution:
    def rob(self, nums: List[int]) -> int:

        # An inefficient method
        # def backtrack(i):
        #     if i > len(nums)-1:
        #         return 0
            
        #     else: return max(nums[i] + backtrack(i + 2), backtrack(i+1))

        # return backtrack(0)

        # A good implementation
        if len(nums) <= 2:
            return max(nums)
        answers = [0]*len(nums)
        answers[0] = nums[0]
        answers[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            answers[i] = max(answers[i-1], nums[i] + answers[i-2])
        return answers[-1]

        # A more efficient implementation regarding space complexity

        rob1, rob2 = 0, 0
        for val in nums:
            temp = max(val + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        