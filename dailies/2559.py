class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        vowels = {'a','e','i','o','u'}
        a = []

        for word in words:
            if (word[-1] in vowels) and (word[0] in vowels):
                # print(word) 
                a.append(1)
            else:
                a.append(0)

        # prefix= [a[0]]
        # for i in range(1,len(a)):
        #     prefix.append(prefix[i-1] + a[i-1])

        prefix = [0] * (len(a) + 1)
        for i in range(len(a)):
            prefix[i + 1] = prefix[i] + a[i]

        print(prefix)

        ans = []
        for i1, i2 in queries:
            ans.append(prefix[i2 + 1] - prefix[i1])

        return ans
        

if __name__ == '__main__':
    solution = Solution()

    testcases = [
        [["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]]],
        [["a","e","i"],[[0,2],[0,1],[2,2]]]
    ]

    for testcase in testcases:
        r = solution.vowelStrings(testcase[0], testcase[1])
        print(r)
        print()