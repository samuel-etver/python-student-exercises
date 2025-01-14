# exercise 002 (LC49)


def group_anagrams(strs):
    result = {}
   
    for s in strs:
        key = create_key(s)
        result[key] = result.get(key, []) + [s]

    return list(result.values())


def create_key(s):
    counts = [0] * 26

    for ch in s:
        index = ord(ch) - ord('a')
        counts[index] += 1
  
    return tuple(counts)


def test(strs):
    print('Input: {}'.format(strs))
    result = group_anagrams(strs)
    print('Output: {}'.format(result))
    print('-' * 3)


strs = ['save',
        'vase',
        'stone',
        'act',
        'lemon',
        'cat',
        'eat',
        'notes',
        'tea',
        'ate',
        'melon',
        'bat']
test(strs)


strs = ['aabb',
        'abab',
        'bbaa',
        'baab',
        'cccc',
        'star',
        'rats']
test(strs)
