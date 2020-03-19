class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_charmap = self.createCharMap(p)
        result = []
        if len(s) >= len(p):
            potential_anagram = ""
            for idx in range(len(p)):
                potential_anagram += s[idx]
            pa_charmap = self.createCharMap(potential_anagram)
            if pa_charmap == s_charmap:
                result.append(0)
            for idx in range(len(p), len(s)):
                pa_charmap = self.updateCharMap(pa_charmap, s[idx - len(p)], s[idx])
                if pa_charmap == s_charmap:
                    result.append(idx - len(p) + 1)
        return result
            
    
    def createCharMap(self, s):
        char_num_arr = [0 for _ in range(26)]
        for ch in s:
            char_num_arr[ord(ch) - ord('a')] += 1
        return char_num_arr
    
    def updateCharMap(self, char_map, remove, add):
        char_map[ord(add) - ord('a')] += 1
        char_map[ord(remove) - ord('a')] -= 1
        return char_map
        
        
        
        