# exercise 001


def is_anagram(s, p):
    if len(s) != len(p):
        return False

    s = s.lower()
    p = p.lower()
    
    counts = [0] * 26

    calc_index = lambda ch : ord(ch) - ord('a')

    for ch in s:
        index = calc_index(ch)
        counts[index] += 1

    for ch in p:
        index = calc_index(ch)
        if counts[index] == 0:
            return False
        counts[index] -= 1
    
    return True


def test(s, p):
    result = is_anagram(s, p)
    print('\'{0}\' is an anagram of \'{1}\': {2}'.format(s, p, result))


test('Fired', 'Fried')
test('Listen', 'Silent')
test('Cafe', 'Face')
test('Planet', 'Heart')
test('Parrot', 'Carrot')
test('aaba', 'bbaa')

      

