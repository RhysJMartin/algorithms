import math


def multiply(x, y):
    print('multiply: {} * {}'.format(x,y))
    if number_of_digits(x) == 1 | (number_of_digits(y) == 1):
        result = x * y
    else:
        m = calculate_right_digits(x, y)
        print('splitting x: {} and y: {}'.format(x, y))
        a, b = split(x, m)
        c, d = split(y, m)
        print('combine: a: {}, b: {}, c: {}, d: {}'.format(a, b, c, d))
        result = combine(a, b, c, d, m)
        print('result: {}'.format(result))
    return result


def calculate_right_digits(x, y):
    len_x = number_of_digits(x)
    len_y = number_of_digits(y)
    return max(len_x, len_y) // 2


def split(x, m):
    a = x // (10 ** m)
    b = x % (10 ** m)
    return a, b


def combine(a, b, c, d, m):
    """ function combines the sub parts of the karatsuba multiplication
    Step 1 compute a * c
    Step 2 compute b * d
    Step 3 compute (a + b)(c + d)
    Step 4 compute (3)-(2)-(1)"""
    s1 = multiply(a, c)
    s2 = multiply(b, d)
    s3 = multiply(a + b, c + d) - s2 - s1
    return s1 * (10 ** (2 * m)) + s3 * (10 ** m) + s2


def number_of_digits(x):
    if x > 0:
        return int(math.log(x, 10)) + 1
    elif x == 0:
        return 1
    elif x < 0:
        raise ValueError


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(multiply(x, y))
