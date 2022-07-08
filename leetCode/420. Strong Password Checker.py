import re
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        solution = 0
        length = len(password)
        for i in range(0, length):
            