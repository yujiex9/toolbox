class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def reverse(self):
        if self.is_empty():
            return
        self.bottom_up()
        peak = self.pop()
        self.reverse()
        self.push(peak)

    def bottom_up(self):
        if self.is_empty():
            return
        peak = self.pop()
        if not self.is_empty():
            self.bottom_up()
            peak_ = self.pop()
            self.push(peak)
            self.push(peak_)
        else:
            self.push(peak)

    @property
    def peak(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)
