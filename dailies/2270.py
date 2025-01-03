class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        len_nums = len(nums)

        a = [0] * (len_nums-1)
        b = [0] * (len_nums-1)

        a[0] = nums[0]
        b[0] = nums[len_nums-1]

        for i in range(1,len_nums-1):
            a[i] = a[i-1] + nums[i]
            b[i] = b[i-1] + nums[len_nums-i-1]
        

        ans = 0
        for i in range(len_nums-1):
            if a[i] >= b[len_nums-i-2]:
                ans += 1

        return ans 

if __name__ == '__main__':
    testcases = [
        [10,4,-8,7],
        [2,3,1,0]
    ]

    solution = Solution()
    
    for testcase in testcases:
        r = solution.waysToSplitArray(testcase)
        print(r)