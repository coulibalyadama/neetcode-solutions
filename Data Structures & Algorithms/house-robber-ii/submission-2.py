class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_houses(num):
            if len(num) == 0:
                return 0
            if len(num) == 1:
                return num[0]

            answers = [0]*len(num)
            answers[0], answers[1] = num[0], max(num[0], num[1])

            for i in range(2, len(num)):
                answers[i] = max(num[i]+answers[i-2], answers[i-1])
            return answers[-1]
        return max(rob_houses(nums[:-1]), rob_houses(nums[1:]))


        
        