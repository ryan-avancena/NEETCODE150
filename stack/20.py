class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parenthesis_dict = { 
            ')' : '(', 
            '}' : '{', 
            ']' : '['}

        stack = []

        for c in s:
            if (c == '(') or (c == '{') or (c == '['):
                stack.append(c)
            elif not stack or parenthesis_dict[c] != stack[-1]:
                return False
            else:
                stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    testcases = [
        "()",
        "()[]{}",
        "(]",
        "([])",
        "["
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.isValid(testcase)
        print(r)