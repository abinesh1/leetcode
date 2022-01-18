class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        left = 0
        right = n-1
        for i in range(n-1, -1, -1):
            if(abs(nums[left])>abs(nums[right])):
                num = nums[left]
                left = left + 1
            else:
                num = nums[right]
                right -= 1
            result[i] = num*num
        return result