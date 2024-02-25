class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def pop(self, index=None):
        if index is None:
            return self.items.pop()
        else:
            return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]


unsorted_list = UnsortedList()

unsorted_list.append(1)
unsorted_list.append(3)
unsorted_list.append(2)

print(unsorted_list.index(2))

print(unsorted_list.pop())

unsorted_list.insert(0, 0)

print(unsorted_list.slice(1, 3))