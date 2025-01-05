class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1_idx = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []


        for i in range(len(nums2)):
            cur = nums2[i] 
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_idx[val]
                res[idx] = cur
            if cur in nums1_idx:
                stack.append(cur)
        
        return res

        

if __name__ == '__main__':
    testcases = [
        [[4,1,2],[1,3,4,2]],
        [[2,4],[1,2,3,4]],
        [[4,1,2],[2,1,3,4]],
    ]

    solution = Solution() 

    for testcase in testcases:
        res = solution.nextGreaterElement(testcase[0],testcase[1])
        print(res)