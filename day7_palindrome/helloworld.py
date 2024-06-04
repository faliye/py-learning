
from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        sign=False
        result = Counter([i for i in s])
        for i in result.values():
            if(i%2 ==0):
                count+=i
            else:
                count+=i-1
                sign = True
        if(sign):
            return count+1
        return count
        
print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("bananas"))
print(Solution().longestPalindrome("ccc"))
print(Solution().longestPalindrome("cc"))
print(Solution().longestPalindrome("c"))



# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dist = {}
#         for i in s:
#             dist[i] = dist.get(i,0)+1
#         count = 0
#         sign=False
#         for i in dist.values():
#             if(i%2 ==0):
#                 count+=i
#             else:
#                 count+=i-1
#                 sign = True
#         if(sign):
#             return count+1
#         return count