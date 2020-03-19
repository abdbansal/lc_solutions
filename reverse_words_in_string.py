class Solution(object):
    
    def reverseString(self, s, start, length):
    
        for i in range(0,(length/2)):
            i_e = start + length - i - 1
            i_char = s[i + start]
            i_e_char = s[i_e]
            new_s = s[:i + start] + i_e_char + s[i + start + 1:i_e]
            if i_e + 1 < len(s):
                new_s += i_char + s[i_e + 1:]
            else:
                new_s += i_char
            s = new_s
        return s
    
    def removeExtraSpace(self, s):
        new_s = ""
        for i in range(len(s)):
            if s[i] == " " and new_s[len(new_s) - 1] != s[i]:
                new_s += s[i]
            elif s[i] != " ":
                new_s += s[i]
        return new_s
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        s = s.strip()
        s = self.reverseString(s, 0, len(s))
        length = 0
        for i in range(len(s)):
            if s[i] != " ":
                length += 1
            elif length > 0:
                s = self.reverseString(s, i - length, length)
                length = 0
        if length > 0:
            s = self.reverseString(s, len(s) - length, length)
        s = self.removeExtraSpace(s)
            
        return s
    
    
    
        
    
    
    
        