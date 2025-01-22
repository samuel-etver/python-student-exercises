# exercise 008


def two_maximums(nums):
    if nums[1] < nums[0]:
        max1, max2 = nums[0], nums[1]
    else:
        max1, max2 = nums[1], nums[0]

    for v in nums[2:]:
        if v > max1:
            max2 = max1
            max1 = v
        elif v > max2:
            max2 = v
        
    return (max1, max2)


def test(nums):
    max1, max2 = two_maximums(nums)
    print('Input: {}'.format(nums))
    print('The first maximum: {}'.format(max1))
    print('The second maximum: {}'.format(max2))
    print('-' * 3)


test([1, 0, 3])
test([1, 5, 3, 4, 2])
test([0, 1, 2, 3, 5, 6, 7, 8])
test([9, 6, 4, 2, 3, 5, 7, 0, 1])

