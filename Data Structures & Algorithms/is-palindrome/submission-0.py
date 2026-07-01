class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():  #only keep this character if it's a letter or number
                newStr += c.lower()

        return newStr == newStr[::-1]
        