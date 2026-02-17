import random
import bisect

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self):
        target = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, target)
        x1, y1, x2, y2 = self.rects[idx]
        prev = self.prefix[idx - 1] if idx > 0 else 0
        offset = target - prev - 1
        width = x2 - x1 + 1
        return [x1 + offset % width, y1 + offset // width]
