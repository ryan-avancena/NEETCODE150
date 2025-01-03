class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers)-1

        while left < right:
            inverse = target - numbers[left]
            if numbers[right] > inverse:
                right -= 1
            elif numbers[right] < inverse:
                left += 1
            else:
                return [left+1,right+1]
            


if __name__ == '__main__':
    testcases = [
        [[2,7,11,15],9],
        [[2,3,4],6],
        [[-1,0],-1]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.twoSum(testcase[0],testcase[1])
        print(r)