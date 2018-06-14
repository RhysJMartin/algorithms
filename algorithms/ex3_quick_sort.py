import os


def load_data(file_name):
    file = os.path.join(os.path.dirname(__file__), '..' , 'data', file_name)
    print('loading file: {}'.format(file))
    data_file = open(file, 'rb')
    data = []
    for line in data_file:
        data.append(int(line))
    return data


def quick_sort(a, l=None, r=None, pivot_mode='first'):
    if l is None:
        l = 0
    if r is None:
        r = len(a)
    if (r - l) <= 1:
        evaluations = 0
        return a, evaluations
    else:
        a = swap_pivot(a, l, r, pivot_mode)
        a, pi = partition(a, l, r)
        evaluations = r - l - 1
        #print('evaluations: {}'.format(evaluations))
        a, evaluations_left = quick_sort(a, l, pi, pivot_mode)
        a, evaluations_right = quick_sort(a, pi + 1, r, pivot_mode)
        evaluations = evaluations + evaluations_left + evaluations_right
        return a, evaluations


def swap_pivot(a, l, r, mode):
    if mode == 'first':
        return a
    elif mode == 'last':
        a[l], a[r-1] = a[r-1], a[l]
        return a
    elif mode == 'median':
        pivot, index = find_median_pivot(a, l, r)
        a[l], a[index] = a[index], a[l]
        return a
    else:
        raise ValueError('Pivot mode: "{}" is not recognised. Expected pivot mode: "first", "last"'.format(mode))


def find_median_pivot(a, l, r):
    mid_index = (r - l - 1) // 2 + l
    pivots = [(a[l], l), (a[mid_index], mid_index), (a[r - 1], r - 1)]
    #print(pivots)
    pivots = sorted(pivots, key=lambda x: x[0])
    #print(pivots)
    return pivots[1]


def partition(a, l, r):
    p = a[l]
    i = l + 1
    #print('start        : {}'.format(a))
    #print('pivot: {}, range: {}'.format(p, a[l:r]))
    for j in range(l + 1, r):
        if a[j] < p:
            # A[j] represents the element that we are testing, A[i] is the first member of the "greater than p" group
            # (or and unsorted value if the size of "greater than p" group is zero).
            a[j], a[i] = a[i], a[j]
            #print('after swap   : {}'.format(a))
            i += 1
    # place the pivot in the correct place
    a[l], a[i - 1] = a[i - 1], a[l]
    #print('return       : {}'.format(a))
    return a, i - 1

if __name__ == '__main__':
    print('Q1')
    data = load_data('QuickSort.txt')
    sorted_data, evaluations = quick_sort(data)
    print(sorted_data)
    print(evaluations)

    print('Q2')
    data = load_data('QuickSort.txt')
    sorted_data, evaluations = quick_sort(data, pivot_mode='last')
    print(sorted_data)
    print(evaluations)

    print('Q3')
    data = load_data('QuickSort.txt')
    sorted_data, evaluations = quick_sort(data, pivot_mode='median')
    print(sorted_data)
    print(evaluations)

