class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return -1 if (m:=(sentence:=' '+sentence).find(' '+searchWord))==-1 else 1+sentence[:m].count(' ')