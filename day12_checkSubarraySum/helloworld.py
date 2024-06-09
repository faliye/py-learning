"""
失败

index   0    1    2    3    4     5     6     7   10   11    12
num    23    2    4    6    7    11    18    24    3    2     7
sum    23   25   29   35   42    53    71    95   98  100   107
%       5    1    5    5    0     5     5     5    2    4     5
       -1         -    -          -     -     -               -
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {0: -1}  # To handle the case where the sub-array starts from index 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            print(i)
            if rem in map:
                
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False
    
# print(Solution().checkSubarraySum([23,2,6,4,7],6))
print(Solution().checkSubarraySum([23,2,4,6,7],6))
# print(Solution().checkSubarraySum([23,2,6,4,7],13))
# print(Solution().checkSubarraySum([23,2,4,6,7],24))
# print(Solution().checkSubarraySum([1,2,12],6))