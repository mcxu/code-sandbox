"""
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. 
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: 
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""
import time

class DCP57:
    def break_string_1(self, s, k):
        s_split = s.split(" ")
        sections = []
        k_count = 0
        section = ""
        while s_split:
            curr_word = s_split.pop(0)
            curr_word_w_space = curr_word + " "
            section += curr_word_w_space
            k_count += len(curr_word_w_space)

            if k_count > k:
                section_trimmed = section.strip()

                if len(section_trimmed) > k:
                    section = section[:-len(curr_word_w_space)] + " "
                    k_count = len(section)
                    s_split.insert(0, curr_word)
                    sections.append(section.strip())
                elif len(section_trimmed) == k:
                    k_count = len(section_trimmed)
                    sections.append(section_trimmed)

                section = ""
                k_count = 0
                
            elif k_count == k:
                sections.append(section.strip())
                section = ""
                k_count = 0

            elif not s_split:
                if len(curr_word) <= k:
                    sections.append(curr_word)

        return sections


    def test1(self):
        s = "the quick brown fox jumps over the lazy dog"
        k = 10
        expected = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
        result = self.break_string_1(s, k)
        print("result: ", result)
        assert result == expected

    def test2(self):
        s = "A skilled engineer can spot if someone knows what they are talking about or not, the coding problem should be irrelevant with regards to getting the job as the job will not be a set of leetcode challenges"
        k = 30
        result = self.break_string_1(s, k)
        print("result: ", result)
        expected = ['A skilled engineer can spot if', 'someone knows what they are', 'talking about or not, the', 'coding problem should be', 'irrelevant with regards to', 'getting the job as the job', 'will not be a set of leetcode', 'challenges']
        assert result == expected

dcp = DCP57()
# dcp.test1()
dcp.test2()