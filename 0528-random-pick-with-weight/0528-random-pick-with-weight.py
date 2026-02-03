import bisect, random

class Solution:
    def __init__(self, w):
        self.prefix = []
        s = 0
        for x in w:
            s += x
            self.prefix.append(s)
        self.total = s

    def pickIndex(self):
        r = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, r)
