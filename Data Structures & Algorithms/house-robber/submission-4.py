class Solution:
    def rob(self, nums: List[int]) -> int:

        # An inefficient method
        # def backtrack(i):
        #     if i > len(nums)-1:
        #         return 0
            
        #     else: return max(nums[i] + backtrack(i + 2), backtrack(i+1))

        # return backtrack(0)
        if len(nums) <= 2:
            return max(nums)
        answers = []
        answers.append(nums[0])
        answers.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            answers.append(max(answers[i-1], nums[i] + answers[i-2]))
        
        return answers[-1]
        