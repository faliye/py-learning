words = ["bella","label","roller"]

"""

630ms
Beats 5.69%

"""

# class Solution(object):
#     def commonChars(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         length = len(words)
#         length_word =  len(words[0])
#         rtype = []
#         words_arr = [ [i for i in word]  for word in words]
#         for i  in range(length-1):
#             for j in range(length_word):
#                 if(words_arr[0][j] not in words_arr[i+1]):
#                     words_arr[0][j] = False
#                 else:
#                     for k in  range(len(words_arr[i+1])):
#                         if(words_arr[i+1][k] == words_arr[0][j]):
#                             words_arr[i+1][k] =  False
#                             break
#             if(any(words_arr[0]) == False):
#                 return  []
#         for i in range(length_word):
#             if(words_arr[0][i] != False):
#                 rtype.append(words_arr[0][i])
#         return rtype

# print(Solution().commonChars(words))
# print(Solution().commonChars(["cool","lock","cook"]))