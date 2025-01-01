import re 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        s = s.replace(" ","")
        s = re.sub("_","",s)
        s = re.sub(r'[^\w\s]', '', s)

        left = 0
        right = len(s) - 1 

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1 
            right -= 1

        return True



if __name__ == '__main__':
    testcases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "racecar",
        " ",
        "  ",
        "ab",
        "bb",
        "ab_a"
    ]

    solution = Solution()

    for testcase in testcases:
        r = solution.isPalindrome(testcase)
        print(r)