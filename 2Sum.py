class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[None for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] in l:
                return [l.index(nums[i]),i]
            l[i]=target-nums[i]
