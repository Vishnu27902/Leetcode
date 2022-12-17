class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=int(len(nums)/3)
        s=list(set(nums))
        temp=[]
        for i in s:
            if nums.count(i)>l:
                temp.append(i)
        return temp
