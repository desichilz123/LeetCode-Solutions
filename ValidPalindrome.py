class Solution(object):
    def isalphanumeric(self, c):
        if (c.isnumeric()):
            return True
        else:
            o = ord(c)
            return (o >= 65 and o <= 90) or (o >= 97 and o <= 122)
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while (l <= r):
            if (not self.isalphanumeric(s[r])):
                r -= 1
            elif (not self.isalphanumeric(s[l])):
                l += 1
            else:
                if (s[l].lower() != s[r].lower()):
                    return False
                l += 1
                r -= 1
        return True