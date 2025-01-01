class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        if s[n-1] == '1':
            right = [1]
        else:
            right = [0]
        
        j = 1
        for i in range(n-2, 0, -1):
            if s[i] == '1':
                right.append(right[j-1]+1)
            else:
                right.append(right[j-1])
            j += 1
        

        if s[0] == '0':
            left = [1]
        else:
            left = [0]

        j = 1 
        for i in range(1,n-1):
            if s[i] == '0':
                left.append(left[j-1]+1)
            else:
                left.append(left[j-1])
            j+=1


        # print(left,right)
        m = 0
        for i in range(n-1):
            m = max(m,left[i] + right[n-i-2])
        return m

if __name__ == '__main__':
    solution = Solution()
    testcases = [
        "011101",
        "00111",
        "1111"
    ]

    for testcase in testcases:
        r = solution.maxScore(testcase)
        print(r)