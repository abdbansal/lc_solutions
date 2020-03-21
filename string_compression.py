class Solution:
    def compress(self, chars: List[str]) -> int:

        idx_one = 0
        # variable for changing length
        length = len(chars)
        # if char before last
        while idx_one < length - 1:
            # idx_one is surely char
            curr_ch = chars[idx_one]
            # idx_two reaches last character
            idx_two = idx_one + 1
            while idx_two < length and curr_ch == chars[idx_two]:
                chars[idx_two] = str(idx_two - idx_one + 1)
                idx_two += 1
            # brings idx_two to last curr_ch
            idx_two -= 1
            # more than one occurence of curr_ch
            if idx_two - idx_one >=  1:
                # pop all small count
                for i in range(idx_two - idx_one - 1):
                    chars.pop(idx_one + 1)
                    length -= 1
                # fix for large numbers 
                if int(chars[idx_one + 1]) > 9:
                    count = chars[idx_one + 1]
                    base = 10
                    length += len(count) - 1
                    chars.pop(idx_one + 1)
                    for i in range(len(count)):
                        chars.insert(idx_one + 1 + i,count[i])
                    idx_one += len(count) + 1
                else:
                    idx_one += 2
            else:
                idx_one += 1
      
        return len(chars)
        