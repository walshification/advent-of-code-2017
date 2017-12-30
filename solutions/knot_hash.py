from collections import deque
import functools
import itertools


class Knot:
    def __init__(self, lengths=None, hash_string=None):
        self._string = deque(hash_string or range(256))
        self.current_position = 0
        self.skip_size = 0
        if lengths is None:
            self.lengths = []
        else:
            self.lengths = [
                ord(c) for c in ','.join(str(i) for i in lengths)
            ] + [17, 31, 73, 47, 23]
        self._hash = None

    @property
    def hash(self):
        if self._hash is None:
            sparse_hash = self.create_sparse_hash()
            dense_hash = self.create_dense_hash(sparse_hash)
            self._hash = self.hexadecimalize(dense_hash)
        return self._hash

    def create_sparse_hash(self):
        for _ in range(64):
            self.twist(self.lengths)
        return self._string

    def twist(self, lengths=None):
        hash_string = self._string
        for length in (lengths or self.lengths):
            hash_string = self._twist_by_length(hash_string, length)
        self._string = hash_string
        return self._string

    def create_dense_hash(self, sparse_hash):
        dense_hash = []
        start = 0
        while start < len(sparse_hash):
            dense_hash.append(self._xor(itertools.islice(sparse_hash, start, start+16)))
            start += 16
        return dense_hash

    def hexadecimalize(self, dense_hash):
        return ''.join('%0.2x' % i for i in dense_hash)

    def _twist_by_length(self, hash_string, length):
        twisted = self._reverse_substring(hash_string, length)
        self.current_position = (
            self.current_position + length + self.skip_size) % len(hash_string)
        self.skip_size += 1
        return twisted

    def _reverse_substring(self, hash_string, length):
        hash_string.rotate(-self.current_position)
        hash_string.extendleft([hash_string.popleft() for i in range(length)])
        hash_string.rotate(self.current_position)
        return hash_string

    def _xor(self, sparse_hash_slice):
        return functools.reduce(lambda a, b: a ^ b, sparse_hash_slice)


if __name__ == '__main__':
    test_input = [189, 1, 111, 246, 254, 2, 0, 120, 215, 93, 255, 50, 84, 15, 94, 62]
    knot = Knot(test_input)
    print('Part One:', knot.twist()[0] * knot.twist()[1])
    knot2 = Knot(test_input)
    print('Part Two:', knot2.hash)
