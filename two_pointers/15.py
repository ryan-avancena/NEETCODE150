from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """ HAD TO WATCH VIDEO :( """
        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
                


        """ OLD ATTEMPT 

        def twoSum(nums, i, target):
            d = {}

            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    inverse = target - nums[j]
                    if inverse in d:
                        return [inverse,nums[j]]
                    d[nums[j]] = j
            
            return

        nums = sorted(nums)
        p = 0 
        solutions = []
        for p in range(1,len(nums)):
            target = 0 - nums[p]
            if nums[p] == nums[p-1]:
                continue
            else:
                for i in range(1,len(nums)):
                    r = twoSum(nums, i, target)
                    if r:
                        r.append(nums[p])
                        if r in solutions:
                            continue
                        else:
                            solutions.append(r)

        return solutions

        """
            
        

if __name__ == '__main__':
    testcases = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.threeSum(testcase)
        print(r)