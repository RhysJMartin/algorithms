import os
from heapq import heappush, heappop


def load_data():
    file = os.path.join(os.path.dirname(__file__), '..', 'data', 'Median.txt')
    print('loading file: {}'.format(file))
    data_file = open(file, 'rb')
    data = []
    for line in data_file:
        data.append(int(line))
    return data


class Median:
    def __init__(self):
        self.low_heap = []
        self.high_heap = []

    def _push_low(self, value):
        heappush(self.low_heap, - value)
        return None

    def _pop_low(self):
        return - heappop(self.low_heap)

    def _push_high(self, value):
        heappush(self.high_heap, value)
        return None

    def _pop_high(self):
        return heappop(self.high_heap)

    def peek_low(self):
        return - self.low_heap[0]

    def add(self, value):
        if len(self.low_heap) == 0:
            self._push_low(value)
        elif len(self.high_heap) == 0:
            self._push_low(value)
        elif value <= self.high_heap[0]:
            self._push_low(value)
        elif value > self.high_heap[0]:
            self._push_high(value)
        self.rebalance()
        return self.peek_low()

    def rebalance(self):
        len_dif = len(self.low_heap) - len(self.high_heap)
        if len_dif == 2:
            value = self._pop_low()
            self._push_high(value)
        if len_dif == -1:
            value = self._pop_high()
            self._push_low(value)
        return None


if __name__ == '__main__':
    data = load_data()
    median = Median()
    medians = [median.add(x) for x in data]
    print(sum(medians))
