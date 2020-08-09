
def my_for(iterable):
    if getattr(iterable, "__iter__", None):
        iterator = iterable.__iter__()

        while True:
            try:
                value = next(iterator)
                print(value)
            except StopIteration:
                break
    elif getattr(iterable, "__getitem__", None):
        index = 0
        while True:
            try:
                print(iterable[index])
                index += 1
            except IndexError:
                break
    else:
        raise TypeError("object is not iterable ")
