"""

Initial Solution: Intuition was there but time complexity was not good :(

1. Create tuple with all 26 letters, where index corresponds to count of a specific letter ~ ORRRR ~ 
2. Sort the string instead of the dictionary.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}

        for str in strs:
            letter_counter = {}
            for letter in str:
                if letter in letter_counter:
                    letter_counter[letter] += 1
                else:
                    letter_counter[letter] = 1

            sorted_letter_count = sorted(letter_counter.items())
            letter_tuple = tuple(sorted_letter_count)
            if letter_tuple not in words:
                words[letter_tuple] = [str]
            else:
                words[letter_tuple].append(str)

        return words.values()
    
    # def betterGroupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
       

if __name__ == '__main__':
    solution = Solution()
    
    testcases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"]
    ]

    for testcase in testcases:
        r = solution.groupAnagrams(testcase)
        print(r)