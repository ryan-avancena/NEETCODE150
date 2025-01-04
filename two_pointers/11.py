class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height)-1
        h = 0
        i = len(height)-1

        while left < right:
            temp = min(height[left],height[right]) * i 
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1 
                right -= 1
                i -= 1
            i -= 1  
            h = max(h,temp)

        return h
        

if __name__ == '__main__':
    testcases = [
        [1,8,6,2,5,4,8,3,7],
        [1,1],
        [1,3,2,5,25,24,5]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.maxArea(testcase)
        print(r)
        print()