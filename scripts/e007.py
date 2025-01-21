# exercise 007 (LC268)


def missing_number(nums):
    sum_of_elements = sum(nums)

    n = len(nums)
    expected_sum = (n * (n + 1)) // 2

    return expected_sum - sum_of_elements


def test(nums):
    v = missing_number(nums)
    print('Input: {}'.format(nums))
    print('Missing number: {}'.format(v))
    print('-' * 3)


test([1, 0, 3])
test([1, 2, 3, 4, 5])
test([0, 1, 2, 3, 5, 6, 7, 8])

