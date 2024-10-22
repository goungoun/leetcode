# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system

from typing import List

class Trie:
    def __init__(self):
        self.root = {}
    
    def build(self, words:List[str])-> None: 
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
                
            curr['<END>'] = ''
                
        return
    
    def startsWith(self, node, prefix, cutoff=3):
        ret = []
        tmp = []

        for c in prefix:
            if c not in node:
                return []
            node = node[c]

        def dfs(node):
            if len(ret) == cutoff:
                return

            for key in node:
                if key != '<END>':
                    tmp.append(key)
                    dfs(node[key])
                    tmp.pop()
                else:
                    ret.append(prefix + "".join(tmp))
                    
        dfs(node)
                    
        return ret

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        t = Trie()
        t.build(products)

        ret = []
        
        for i in range(1, len(searchWord)+1):
            search = t.startsWith(t.root, searchWord[:i])
            ret.append(search)

        return ret
