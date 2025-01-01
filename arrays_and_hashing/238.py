class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n 
        suffix = [1] * n 
        prod = [1] * n 
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix [i-1]
         
            
        for i in range(n-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        
        for i in range(n):
            prod[i] = prefix[i] * suffix[i]

        return prod

        

if __name__ == '__main__':
    solution = Solution()
    
    testcases = [
        [1,2,3,4],
        [-1,1,0,-3,3]
    ]

    for testcase in testcases:
        r = solution.productExceptSelf(testcase)
        print(r)