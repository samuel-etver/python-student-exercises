# exercise 005 (LC28)


def index_of_substr(needle, haystack):
    needle_len = len(needle)
    haystack_len = len(haystack)

    if needle_len > haystack_len:
        return -1

    for index in range(0, haystack_len - needle_len + 1):
        if haystack[index : index + needle_len] == needle:
            return index

    return -1


def test(needle, haystack):    
    result = index_of_substr(needle, haystack)
    print('Index of first occurence \'{}\' in \'{}\': {}'. \
          format(needle, haystack, result))


test('abc', 'abcxyzabc')
test('abc', 'xyzabcabc')
test('abc', 'xyz')
test('abc', 'yzabcx')
test('sadbutsad', 'sad')
