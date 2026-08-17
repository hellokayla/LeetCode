from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_list = list(sentence)
        freq = Counter(sentence_list)
        
        if len(freq.keys()) < 26:
            return False
        else: return True