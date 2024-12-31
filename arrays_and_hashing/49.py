"""

Initial Solution: Intuition was there but time complexity was not good :(

Other

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