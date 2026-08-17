class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0

        for sentence in sentences:
            curr_words = len(sentence.split(" "))
            max_len = max(curr_words, max_len)
        return max_len