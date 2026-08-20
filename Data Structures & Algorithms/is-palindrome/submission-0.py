class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        check = "abcdefghijklmnopqrstuvwxyz1234567890"
        for letter in s:
            if letter.lower() in check:
                string += letter.lower()

        return string == string[::-1]
            