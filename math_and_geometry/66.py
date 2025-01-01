class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)-1
        digits[n] += 1

        

        while digits[n] > 9 and n > 0:
            if digits[n] == 10: 
                print(digits[n])

            n -= 1


        

if __name__ == '__main__':
    testcases = [
        [1,2,3],
        [4,3,2,1],
        [9],
        [9,9]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.plusOne(testcase)
        print(r)