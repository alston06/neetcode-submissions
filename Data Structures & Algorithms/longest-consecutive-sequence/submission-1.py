class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        nums = list(nums)
        streak = 0
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            num = nums[i]
            count = 1
            nextNum = num+1
            for j in range(i+1, len(nums)):
                if nums[j] == nextNum:
                    count = count + 1
                    nextNum = nextNum+1
                    print(nextNum, count)

            if count > streak:
                streak = count
                
        return streak