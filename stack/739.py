from collections import defaultdict

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = []      # [[temp,index]]       
        
        # [73,74,75,71]

        for i,t in enumerate(temperatures):
            # print(i,t)
            while stack and t > stack[-1][0]:
                stackIdx = stack[-1][1]
                res[stackIdx] = i - stackIdx
                stack.pop()
            stack.append([t,i])
        
        return res



        """ FIRST SOLUTION WITH HASMAP, O(n^2) SOLUTION 

        ans = [0] * len(temperatures)
        minimum = 0


        c = defaultdict()       # {index : temperature}
        for i in range(0,len(temperatures)):
            c[i] = temperatures[i] 
            if temperatures[i] > minimum: # if current temperature is greater than minimum
                for key,value in list(c.items()): # iterate through hashmap
                    if value < temperatures[i]:
                        ans[key] = i-key         
                        c.pop(key)
            
        return ans

        """

        

if __name__ == '__main__':
    testcases = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90],
        [70,69,75,71,69,72,76,73],
        [70,69,75,76]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.dailyTemperatures(testcase)
        print(r)