class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        start = 0
        end = len(s) - 1
        # O(n)
        while(start < end):
            if not s[start].isalpha() and not s[start].isdigit():
                start += 1
            elif not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                result = False
                break
        return result