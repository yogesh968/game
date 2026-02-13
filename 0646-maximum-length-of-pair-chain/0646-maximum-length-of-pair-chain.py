# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         count = 1 
#         n = len(pairs)
#         for i  in range(1,len(pairs)):
#             if pairs[i-1][1]==pairs[i][0]:
#                 if (i<=n):
#                     i +=1
#                 return 0
#             if pairs[i-1][1] <  pairs[i][0]:
#                 count+=1
#         return count   
class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        count = 1
        end = pairs[0][1]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                count += 1
                end = pairs[i][1]
        
        return count

        