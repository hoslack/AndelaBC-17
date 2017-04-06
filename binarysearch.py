class BinarySearch(list):
    def __init__(self, a, b):
        self.array = range(b, (a * b) + 1, b)
        self.length = len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def search(self, val):
        count = 0
        first = 0
        last = len(self.array) - 1

        while True:
            if val == self.array[first]:
                return {'index': first, 'count': count}
            elif val == self.array[last]:
                return {'index': last, 'count': count}

            middle = (first + last) // 2

            if val == self.array[middle]:
                return {'index': mid, 'count': count}

            elif val > self.array[middle]:
                first = middle + 1

            elif val < self.array[middle]:
                last = middle - 1

            if first >= last:
                return {'index': -1, 'count': count}

            count += 1

m = BinarySearch(100000, 1)
print m.search(67)
