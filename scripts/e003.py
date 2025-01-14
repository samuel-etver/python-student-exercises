# exercise 003 (LC217)


def has_duplicates(nums):
    return len(nums) > len(set(nums))


def test(nums):
    result = has_duplicates(nums)
    print('List {} has duplicates: {}'.format(nums, result))


nums = [1, 2, 3, 4, 5, 6, 4]
test(nums)

nums = [10, 11, 4, 5, 7]
test(nums)

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
test(nums)

nums = [1, 2, 3, 4]
test(nums)

nums = [1,2,3,1]
test(nums)

