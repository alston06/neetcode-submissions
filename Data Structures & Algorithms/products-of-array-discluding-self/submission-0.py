class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        res = [0]*len(nums)
        
        zeroes = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes+=1
            else:
                prod*=nums[i]

        if zeroes > 1: return res
        for i, c in enumerate(nums):
            if zeroes: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
