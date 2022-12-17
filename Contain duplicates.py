class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ls=set(nums)
        if(len(ls)!=len(nums)):
            return True
        else:
            return False
