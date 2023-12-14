"""
Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax.
"""
class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration

for i in Counter(13,29):
    print(i) 