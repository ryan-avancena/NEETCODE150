class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        counter = {}
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 1

        return False

if __name__ == '__main__':
    solution = Solution()
    
    testcases = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2],
    ]

    for testcase in testcases:
        r = solution.containsDuplicate(testcase)
        print(r)