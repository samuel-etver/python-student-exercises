# exercise 001 (LC242)


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = [0] * 26

    calc_index = lambda ch : ord(ch) - ord('a')

    for ch in s:
        index = calc_index(ch)
        counts[index] += 1

    for ch in t:
        index = calc_index(ch)
        if counts[index] == 0:
            return False
        counts[index] -= 1
    
    return True


def test(s, t):
    result = is_anagram(s, t)
    print('\'{0}\' is an anagram of \'{1}\': {2}'.format(s, t, result))


test('fired', 'fried')
test('listen', 'silent')
test('cafe', 'face')
test('planet', 'heart')
test('parrot', 'carrot')
test('aaba', 'bbaa')

      

