import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        solvent = re.search(p, s)
        print(solvent)
        if (solvent != None) and (s == solvent[0]):
            return True
        return False
print(Solution.isMatch(None, "ab", ".*c"))