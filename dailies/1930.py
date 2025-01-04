from collections import Counter

""" HAD TO WATCH NEETCODE SOLUTION """

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = set()
        right = Counter(s)
        ans_set = set()

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    ans_set.add((s[i],c))

            left.add(s[i])

        return len(ans_set)

        """ FIRST ATTEMPT 
         
        left.add(s[0])
        for i in range(2,len(s)):
            right[s[i]] += 1

        for i in range(1,len(s)):
            mid = s[i]
            for item in left:
                if (item in right) and (right[item] != 0):
                    ans_set.add((item,mid,item))
                    right[item] -= 1

        print(ans_set)
        return len(ans_set)
           
        """
        
if __name__ == '__main__':
    testcases = [
        "aabca",
        "adc",
        "bbcbaba"
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.countPalindromicSubsequence(testcase)
        print(r)