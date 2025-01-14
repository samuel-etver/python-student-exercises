# exercise 004 (LC3)


def len_of_longest_substr(s):
    s = s.lower()
    
    max_len = 0
    indices = {}
    left_index = 0

    for right_index, ch in enumerate(s):
        if (ch in indices) and (indices[ch] >= left_index):            
            left_index = indices[ch] + 1
        max_len = max(max_len, right_index - left_index + 1)
        indices[ch] = right_index
        
    return max_len


def test(s):
    print('Input: \'{}\''.format(s))
    max_len = len_of_longest_substr(s)
    print('Max length of longest substring: {}'.format(max_len))
    print('-' * 3)


test('aa')
test('ab')
test('aba')
test('abcda')
test('abcabcbb')
test('bbbbb')
test('pwwkew')

