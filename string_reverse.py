def string_reverse(s):
    if s is None:
        return None
    return s[::-1]
    # return ''.join(reversed(s))
    # return ''.join( s[i] for i in range(len(s)-1, -1, -1))

print(string_reverse('hogefuga'))
print(string_reverse(None))
print(string_reverse(''))