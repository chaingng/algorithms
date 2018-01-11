class HashTable(object):
    _empty = object()

    def __init__(self, size=10):
        self.size = size
        self._len = 0
        self.keys = [self._empty] * size
        self.values = [self._empty] * size
    
    def hash(self, key):
        return key % self.size
    
    def rehash_(self, old_hash):
        return (old_hash +1) % self.size

    def put(self, key, value):
        init_hash = hash_ = self.hash(key)
        while True:
            if self.keys[hash_] is self._empty:
                self.keys[hash_] = key
                self.values[hash_] = value
                self._len += 1
                return
            elif self.keys[hash_] == key:
                self.values[hash_] = value
                return
            
            hash_ = self.rehash_(hash_)

            # table is full
            if init_hash == hash_:
                return None


    def get(self, key):
        init_hash = hash_ = self.hash(key)
        while True:
            if self.keys[hash_] is self._empty:
                return None
            elif self.keys[hash_] == key:
                return self.values[hash_]
            
            hash_ = self.rehash_(hash_)

            # table is full
            if init_hash == hash_:
                return None

    def delete_(self, key):
        init_hash = hash_ = self.hash(key)
        while True:
            if self.keys[hash_] is self._empty:
                return
            elif self.keys[hash_] == key:
                self.keys[hash_] = self._empty
                self.values[hash_] = self._empty
                self._len -= 1
                return
            
            hash_ = self.rehash_(hash_)

            # table is full
            if init_hash == hash_:
                return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __delitem__(self, key):
        return self.delete_(key)

    def __len__(self):
        return self._len

h = HashTable()
h[3] = 'hoge'
h[4] = 'fuga'
h[13] = 'hogefuga'
print(h[3])
del h[3]
print(h[4])