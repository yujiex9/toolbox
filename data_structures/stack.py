from copy import deepcopy


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        return self.__items.pop()

    def to_list(self):
        # return [self.pop() for i in range(len(self))]
        return deepcopy(self.__items)

    def bottom_up(self):
        if self.is_empty():
            return
        peak = self.pop()
        if self.is_empty():
            self.push(peak)
        else:
            self.bottom_up()
            _peak = self.pop()
            self.push(peak)
            self.push(_peak)

    def move_min_to_peak(self):
        if self.is_empty():
            return
        peak = self.pop()
        if not self.is_empty():
            self.move_min_to_peak()
            if self.peak <= peak:
                _peak = self.pop()
                self.push(peak)
                self.push(_peak)
                return
        self.push(peak)

    def reverse(self):
        if self.is_empty():
            return
        self.bottom_up()
        peak = self.pop()
        self.reverse()
        self.push(peak)

    def sort(self):
        # 1 5 3 4 2
        if self.is_empty():
            return
        self.move_min_to_peak()
        peak = self.pop()
        self.sort()
        self.push(peak)

    @property
    def peak(self):
        if not self.is_empty():
            return self.__items[-1]

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        pass

    @classmethod
    def from_list(cls, seq):
        _stack = cls()
        for item in seq:
            _stack.push(item)
        return _stack
