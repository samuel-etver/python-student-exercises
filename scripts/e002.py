# exercise 002


def group_anagrams(strs):
    result = {}
   
    for s in strs:
        key = create_key(s)
        result[key] = result.get(key, []) + [s]

    return list(result.values())


def create_key(s):
    s = s.lower()
    
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


strs = ['Save',
        'Vase',
        'Stone',
        'Act',
        'Lemon',
        'Cat',
        'Eat',
        'Notes',
        'Tea',
        'Ate',
        'Melon',
        'Bat']
test(strs)


strs = ['aabb',
        'abab',
        'bbaa',
        'baab',
        'cccc',
        'star',
        'rats']
test(strs)
