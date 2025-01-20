# exercise 006 (LC283)


def move_zeroes(nums):
    left_index = 0

    for right_index in range(len(nums)):
        if nums[right_index] != 0:
            nums[right_index], nums[left_index] = \
                nums[left_index], nums[right_index]
            left_index += 1


def test(nums):
    print('Input: {}'.format(nums))
    move_zeroes(nums)
    print('Result: {}'.format(nums))    
    print('---')


test([1, 0, 2, 3, 4, 8, 0, 9, 7])
test([0, 0, 4, 5, 6, 7, 0])
test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
test([0])
test([0, 1])

