from collections import defaultdict
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        if len(strs) == 0: 
            return ""
        ## delimiter: integer followed by # sign

        for word in strs:
            ans = ans+ (str(len(word))+ "#"+ word)
        #print("ans:", ans)
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # use two pointers
        res = []
        i = 0 

        while i < len(s):
            j = i
            # capture the integer value before hashtag
            # j is the location of the hashtag delimiter
            while s[j] != "#":
                j += 1
            # everything before the hashtag
            length = int(s[i:j])
            start = j+1
            res.append(s[start:start+length])
            i = start + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
