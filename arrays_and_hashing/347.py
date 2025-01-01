"""

We're using `heapq` in this method. 

"""
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c = {} 
        for num in nums:
            if num in c:
                c[num] += 1 
            else:
                c[num] = 1
        
        # Use heapq.nlargest with key as the frequency
        r = heapq.nlargest(k, c.keys(), key=c.get)
        return r
        

if __name__ == '__main__':
    solution = Solution()

    testcases = [
        [[1,1,1,2,2,3],2],
        [[1],1]
    ]

    for testcase in testcases:
        r = solution.topKFrequent(testcase[0],testcase[1])
        print(r)