class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]] += 1
            else:
                count_s[s[i]] = 1
            
            if t[i] in count_t:
                count_t[t[i]] += 1
            else:
                count_t[t[i]] = 1

        return count_s == count_t


if __name__ == '__main__':
    solution = Solution()
    
    testcases = [
        ["anagram","nagaram"],
        ["rat","car"]
    ]

    for testcase in testcases:
        r = solution.isAnagram(testcase[0],testcase[1])
        print(r)