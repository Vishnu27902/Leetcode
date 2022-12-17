class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d={}
        # s=set(nums)
        # for i in s:
        #     d[nums.count(i)]=i
        # return d[max(d.keys())]
        s=set()
        for i in  nums:
            if i in s:
                return i
            s.add(i)
