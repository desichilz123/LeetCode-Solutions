class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        else:
            for char in t:
                s = s.replace(char, '', 1)
            return not s

        