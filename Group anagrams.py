from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        # Return grouped anagrams
        return list(anagram_map.values())
