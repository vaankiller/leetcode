__author__ = 'vaan'

import collections

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False


word_dict = WordDictionary()
word_dict.addWord("how")
word_dict.addWord("are")
word_dict.addWord("you")
word_dict.addWord("damn")
word_dict.addWord("good")
word_dict.addWord("ho")
word_dict.addWord("goo")
print word_dict.search("..")
print word_dict.search("go.d")