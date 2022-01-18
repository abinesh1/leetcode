class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        current = 0
        for i in nums:
          if(i == 1):
            current +=1
          else:
            maxi = max(maxi, current)
            current = 0
        return max(maxi, current)