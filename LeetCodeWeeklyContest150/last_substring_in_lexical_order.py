class Solution:
    def lastSubstring(self, s):
        if s == "":
            return ""
        highest_letter = max(list(s))
        highest_substring = ""
        for pos, letter in enumerate(s):
            if letter == highest_letter:
                highest_substring = max(highest_substring, s[pos:])
        return highest_substring