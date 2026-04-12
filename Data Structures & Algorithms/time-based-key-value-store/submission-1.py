class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        l = 0 
        r = len(self.timeMap[key]) -1
        print(self.timeMap[key])
        while l <= r:
            mid = l + (r - l) // 2

            if self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]
            elif self.timeMap[key][mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if l - 1 >= 0:
            return self.timeMap[key][l-1][0]
        return ""
   