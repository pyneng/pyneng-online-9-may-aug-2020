class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._last_item = start

    def __next__(self):
        print("Работает __next__")
        value = self._last_item
        if self._last_item == self.stop:
            raise StopIteration
        self._last_item += 1
        return value

    def __iter__(self):
        return self

if __name__ == "__main__":
    int_range = MyRange(1, 10)
    for i in int_range:
        print(i)
