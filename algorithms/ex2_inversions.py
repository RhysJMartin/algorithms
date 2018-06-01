import os


def load_data():
    file = os.path.join(os.path.dirname(__file__), '..' , 'data', 'IntegerArray.txt')
    print('loading file: {}'.format(file))
    data_file = open(file, 'rb')
    data = []
    for line in data_file:
        data.append(int(line))
    return data


def sort_and_count(x):
    if len(x) == 1:
        return x, 0
    a, b = split(x)
    sorted_a, left_count = sort_and_count(a)
    sorted_b, right_count = sort_and_count(b)
    sorted_x, split_count = merge_and_count_split_inv(sorted_a, sorted_b)
    count = left_count + right_count + split_count
    return sorted_x, count


def merge_and_count_split_inv(a, b):
    """Assume that list a and b are sorted. Returns a sorted list and count of inversions"""
    items = len(a) + len(b)
    i = 0
    j = 0
    count = 0
    sorted_list = []
    for _ in range(items):
        if (i < len(a)) & (j < len(b)):
            if a[i] < b[j]:
                sorted_list.append(a[i])
                i += 1
            else:
                sorted_list.append(b[j])
                j += 1
                count += len(a) - i
        elif i < len(a):
            sorted_list.append(a[i])
            i += 1
        elif j < len(b):
            sorted_list.append(b[j])
            j += 1
    return sorted_list, count


def split(x):
    n = len(x) // 2
    a, b = x[:n], x[n:]
    return a, b

if __name__ == '__main__':
    x = load_data()
    x_out, count = sort_and_count(x)
    print(x_out)
    print(count)
