# 1268. Search Suggestions System (Medium)
# https://leetcode.com/problems/search-suggestions-system

from typing import List
from collections import OrderedDict

class Trie:
    def __init__(self):
        self.root = OrderedDict()
        self.END = "*"
    
    def build(self, words:List[str]) -> None:
        """
        Build trie (prefix tree)

        T=O(wl), S=(wl)
        * w: num of word (1 <= words.length <= 1000)
        * l: avg length of the words (1 <= word[i].length <= 3000)
        """
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
                
            curr[self.END] = ''
                
        return
    
    def startsWith(self, prefix, cutoff=3) -> List[str]:
        """
        Traverse trie and return words that are started with a given prefix
        return wlist

        T=(l+n)
        * l: the length of prefix (1 <= prefix.length <= 1000)
        * n: num of nodes in the tree
        """
        wlist = []
        tmp = []

        node = self.root

        for c in prefix:
            if c not in node:
                return []
            node = node[c]

        def dfs(node):
            if len(wlist) == cutoff:
                return

            for key in node:
                if key != self.END:
                    tmp.append(key)
                    dfs(node[key])
                    tmp.pop()
                else:
                    wlist.append(prefix + "".join(tmp))
                    
        dfs(node)
                    
        return wlist

class Solution:
    def buildTrie(self, products: List[str]):
        """
        Prepare a data structure - trie optimized for suggests.
        Build once and reuse it. Do not call it directly for enduser typing.
        """
        products.sort() # T=O(nlogn) lexicographical order

        t = Trie()
        t.build(products) # T=O(wl)

        return t

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = self.buildTrie(products)
        suggests = [t.startsWith(searchWord[:i]) for i in range(1, len(searchWord) + 1)]

        return suggests
