import collections 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen =  collections.defaultdict(int)
        win_start = 0 
        max_length = 0
        
        for win_end in range(0, len(s)):
            # repeated characters
            # 1: first time repeated
            if (s[win_end] in seen):
                win_start = max(win_start, seen[s[win_end]]+1)
                print(win_start)
        
             
            seen[s[win_end]] = win_end
            max_length = max(max_length, win_end - win_start + 1)
                
        return max_length