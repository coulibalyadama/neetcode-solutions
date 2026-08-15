class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def rob_houses(num):
            rob1, rob2 = 0, 0

            for val in num:
                temp = max(val + rob2, rob1)
                rob2 = rob1
                rob1 = temp

            return rob1
        return max(nums[0], rob_houses(nums[:-1]), rob_houses(nums[1:]))


        
        