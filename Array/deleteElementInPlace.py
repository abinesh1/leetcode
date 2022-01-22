class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i<n:
            if nums[i] == val:
                del nums[i:i+1]
                nums.append(0)
                n-=1
            else:
                i+=1
        return n
        