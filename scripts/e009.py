# exercise 009


def max_power(s):
    last_ch = s[0]
    count = 1
    max_count = count
    
    for ch in s[1:]:
        if last_ch == ch:
            count += 1
        else:
            last_ch = ch
            count = 1
        max_count = max(max_count, count)
        
    return max_count



def test(s):
    v = max_power(s)
    print('Input: {}'.format(s))
    print('The max power of string: {}'.format(v))
    print('-' * 3)


test('abc')
test('aabcccd')
test('abbbcddeeeeff')
     

