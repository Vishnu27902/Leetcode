class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        d={}
        for i in s:
            d[i]=nums.count(i)
        l=d.keys()
        for i in l:
            if d[i]>int(len(nums)/2):
                return i
