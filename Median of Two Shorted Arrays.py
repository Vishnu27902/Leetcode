class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls=[]
        ls.extend(nums1)
        ls.extend(nums2)
        ls=sorted(ls)
        m=0
        if(len(ls)%2!=0):
            m=ls[int(len(ls)/2)]
            return m
        else:
            m=ls[int(len(ls)/2)-1]+ls[int(len(ls)/2)]
            return m/2
