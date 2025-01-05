import re
import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        operands = []

        for c in tokens:
            if c.lstrip('-').isnumeric():  
                operands.append(int(c))
            else:  
                # if len(operands) < 2:
                #     raise ValueError("Not enough operands for operation.")
                
                b = operands.pop()
                a = operands.pop()
                
                if c == '+':
                    operands.append(a + b)
                elif c == '-':
                    operands.append(a - b)
                elif c == '*':
                    operands.append(a * b)
                elif c == '/':
                    operands.append(int(a / b))

        return int(operands[-1])

        

if __name__ == '__main__':
    testcases = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        ["4","3","-"],
        ["4","-2","/","2","-3","-","-"]
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.evalRPN(testcase)
        print(r)
        print()