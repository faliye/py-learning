class Solution():
    def isNStraightHand(this,hand,groupSize):
        length = len(hand)
        if(length%groupSize != 0):
            return False
        hand = sorted(hand)
        arr = []
        result = []
        i=0
        arr.append(hand[0])
        hand.remove(hand[0])
        
        while True:
            if(len(hand)<1):
                break
            
            if(hand[i] - arr[len(arr)-1] == 1):
                arr.append(hand[i])
                hand.remove(hand[i])
                if(len(arr)==groupSize):
                    result.append(arr)
                    arr = []
                    i =0
                    if(len(hand)<1):
                        break
                    arr.append(hand[i])
                    hand.remove(hand[i])
                else:
                    if(len(hand)>1):
                        i+=1
            if(hand[i] - arr[len(arr)-1] > 1):
               hand[:i]
               i=0
            
        if(len(result)<groupSize):
            return False
        return True 
                
        
# print(Solution().isNStraightHand([1,2,3,2,3,4,6,7,8],3))
print(Solution().isNStraightHand([1,2,3],1))



# class Solution(object):
#     def find_successors(self, hand, groupSize, i, n):
#         next_val = hand[i] + 1
#         hand[i] = -1  # Mark as used
#         count = 1
#         i += 1
#         while i < n and count < groupSize:
#             if hand[i] == next_val:
#                 next_val = hand[i] + 1
#                 hand[i] = -1
#                 count += 1
#             i += 1
#         return count == groupSize

#     def isNStraightHand(self, hand, groupSize):
#         n = len(hand)
#         if n % groupSize != 0:
#             return False
#         hand.sort()
#         for i in range(n):
#             if hand[i] >= 0:
#                 if not self.find_successors(hand, groupSize, i, n):
#                     return False
#         return True