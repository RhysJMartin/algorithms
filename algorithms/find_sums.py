import os
from tqdm import tqdm


def load_data(file_name):
    file = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
    print('loading file: {}'.format(file))
    data_file = open(file, 'rb')
    data = []
    for line in data_file:
        data.append(int(line))
    return data


def count_2_sums(data, interval):
    data_set = set(data)
    count = 0
    for target in tqdm(range(interval[0], interval[1]+1)):
        for test_number in data:
            opposite = target - test_number
            if (opposite in data_set) and opposite != test_number:
                count += 1
                break
    return count


if __name__ == '__main__':
    _data = load_data('2sum.txt')
    _interval = [-10000, 10000]
    print(count_2_sums(_data, _interval))