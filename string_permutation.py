from collections import defaultdict

def string_permutation(s1, s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    
    hash_table = defaultdict(int)
    for letter in s1:
        hash_table[letter] += 1

    for letter in s2:
        hash_table[letter] -= 1

    for k,v in hash_table.items():
        if v != 0:
            return False
    return True


print(string_permutation('act', 'cat'))
print(string_permutation('dog', 'dod'))
print(string_permutation('act', None))
