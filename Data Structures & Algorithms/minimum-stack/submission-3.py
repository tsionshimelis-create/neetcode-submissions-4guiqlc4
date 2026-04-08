class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val - self.min < 0:
                self.min = val
        

    def pop(self) -> None:

        popped = self.stack.pop()

        if popped < 0:
            self.min = self.min - popped
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0: 
            return top + self.min
        return self.min

    def getMin(self) -> int:
        return self.min
