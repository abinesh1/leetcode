class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
          length = 0
          while i>0:
            length+=1
            i = i/10
          if(length%2 == 0):
            count+=1
        return count
        

        ## return sum([len(str(n)) % 2 == 0 for n in nums])