class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counter = {}
        i = 0 
        for num in nums:
            inverse = target - num
            if inverse in counter:
                return [counter[inverse],i]

            counter[num] = i
            i += 1

if __name__ == '__main__':
    solution = Solution()

    testcases = [
        [[2,7,11,15],9],
        [[3,2,4],6],
        [[3,3],6]
    ]

    for testcase in testcases:
        r = solution.twoSum(testcase[0],testcase[1])
        print(r)