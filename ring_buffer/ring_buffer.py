class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        index = self.current % self.capacity
        self.storage[index] = item
        self.current += 1

    def get(self):
        return [i for i in self.storage if i != None]


# test = RingBuffer(3)
# print(3 % test.capacity)

# test.append('a')
# test.append('b')
# test.append('c')
# print(test.storage)
# test.append('d')
# print(test.storage)
