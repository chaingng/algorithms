from nose.tools import assert_equal

class CompressString(object):

    def compress(self, s):
        if len(s) == 0:
            return s
        compressed_string = ''
        last = s[0]
        count = 1
        for i in range(1,len(s)):
            if last == s[i]:
                count += 1
            else:
                compressed_string = compressed_string + last + str(count)
                last = s[i]
                count = 1

        compressed_string = compressed_string + last + str(count)
        if len(compressed_string) < len(s):
            return compressed_string
        return s

class TestCompressString(object):
    def compress_string(self, func):
        assert_equal(func('AAABCCDDDD'), 'A3B1C2D4')
        assert_equal(func(''), '')
        assert_equal(func('AAABCDEFGH'), 'AAABCDEFGH')
        print('test success')

if __name__ == '__main__':
    test = TestCompressString()
    compress_string = CompressString()
    test.compress_string(compress_string.compress)
