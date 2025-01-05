class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        stack = []  # [(position, speed), ...]
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs = sorted(pairs)

        for p,s in pairs[::-1]:
            stack.append((target-p)/s)

            # Check for a collision: if the current car takes less or equal time 
            # than the car in front (closer to the target), they form a fleet.
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop() # Remove the current car's time since it merges with the fleet.
            
        
        return len(stack)



if __name__ == '__main__':
    testcases = [
        [12,[10,8,0,5,3],[2,4,1,1,3]],
        [10,[3],[3]],
        [100,[0,2,4],[4,2,1]]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.carFleet(testcase[0],testcase[1],testcase[2])
        print(r)