# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:
    def __init__(self):
        """
        Implement Trie (Prefix Tree)

        Approach:
        Prepare empty dictionay, and use them as a nested key:value dictionary structure
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Insert "Trie" and "Try"
        + "Trie"
        {'T':{}}
        {'T':{'r':{}}}
        {'T':{'r':{'i':{}}}}
        {'T':{'r':{'i':{'e':{}}}}}
        {'T':{'r':{'i':{'e':{'<END>':''}}}}}

        + Try
        {'T':{'r':{'i':{'e':{'<END>':''}}, 'y':{'<END>':''}}}}
        """
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['<END>'] = ''

    def search(self, word: str) -> bool:
        """
        For each iteration of the letter from a word
        Replace cur trie to the result and relpeat
        If it is successful by the end of the <END> token, return True

        Example 1: Search the woid 
        d = d['T']
        {'r': {'i': {'e': {'<END>': ''}}, 'y': {'<END>': ''}}}

        d = d['r']
        {'i': {'e': {'<END>': ''}}, 'y': {'<END>': ''}}

        search d['y']
        {'i': {'e': {'<END>': ''}, 'y': {'<END>': ''}}}

        retuin True
        """
        d = self.trie

        # "Try" : d['T']['r']['y'] => {'<END>': ''}
        for c in word:
            if c not in d:
                return False
            d = d[c]

        # Must see the <END> token for an exact matching
        return '<END>' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        # "Tr" : d['T']['r']
        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        # It enough without <END> token for startsWith
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
