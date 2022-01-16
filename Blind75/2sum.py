class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictmap = {}
        
        for i, n in enumerate(nums):
          diff = target - n
          if diff in dictmap:
            return [i, dictmap[diff]]
          
          dictmap[n] = i