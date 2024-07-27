# 49. Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group Anagrams

        Example:
        strs = ["eat","tea","tan","ate","nat","bat"]
        return [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        d = defaultdict(list)

        for word in strs:
            # set is not applicable because any char can be used more then twice
            l = [0]*26
            
            for c in word:
                l[ord(c)-ord('a')] += 1
            
            d[tuple(l)].append(word)

        return d.values()
