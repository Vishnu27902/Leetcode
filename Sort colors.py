class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # i=0
        # j=-1
        # for k in range(0,len(nums)):
        #     if(nums[k]==1):
        #         nums[i],nums[k]=nums[k],0
        #         i+=1
        #     elif(nums[k]==2):
        #         nums[j],nums[k]=nums[k],2
        #         k-=1
        # print(nums)
        nums.sort()
        
