import math

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0 
        right = len(nums)-1

        while left <= right:
            mid = (right+left)//2
            print(f'Mid: {mid}')
            if target > nums[mid]:
                left = mid + 1          # we add + one cause it wasn't mid
            elif target < nums[mid]:
                right = mid - 1         # same goes here as well
            elif target == nums[mid]:
                return mid 
                
        return -1

            
        704 

if __name__ == '__main__':
    testcases = [
        [[-1,0,3,5,9,12],9],
        [[-1,0,3,5,9,12],2],
        [[1],1],
        [[1],2]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.search(testcase[0],testcase[1])
        print(r)