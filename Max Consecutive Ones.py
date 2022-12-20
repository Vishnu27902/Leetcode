class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        count=0
        for j in range(len(nums)):
            if(nums[j]==1):
                count+=1
            else:
                count=0
            if(count>max):
                max=count
        return max
            
