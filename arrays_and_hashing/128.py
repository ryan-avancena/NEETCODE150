class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """ CORRECT SOLUTION """

        nums = set(nums)  # Use a set for O(1) lookups

        if not nums:
            return 0

        longest = 0
        for i in nums:
            if i - 1 not in nums:  # Start of a sequence
                j = i
                seq = 0
                while j in nums:
                    seq += 1
                    j += 1
                longest = max(seq, longest)

        return longest


        ''' OLD SOLUTION 

        nums = set(nums)
        nums = list(nums)

        if len(nums) == 0:
            return 0

        longest = 1
        for i in nums:
            if i+1 in nums:
                j = i
                seq = 1  
                while j in nums:
                    if j+1 not in nums:
                        break
                    else:
                        seq += 1 
                    j += 1
                longest = max(seq,longest)     

        return longest

        '''




if __name__ == '__main__':
    testcases = [
        [100,4,200,1,3,2],
        [0,3,7,2,5,8,4,6,0,1],
        [],
        [1,2],
        [1],
        [9,1,4,7,3,-1,0,5,8,-1,6]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.longestConsecutive(testcase)
        print(r)