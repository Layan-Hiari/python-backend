class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

counter = CountUpTo(5)

for number in counter:
    print(number)


def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

for number in count_up_to(7):
    print(number)

