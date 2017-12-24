from collections import deque


class KnotHash:
    def __init__(self, lengths, hash_string=None):
        self._string = deque(hash_string or range(256))
        self.current_position = 0
        self.skip_size = 0
        self.lengths = lengths

    @property
    def string(self):
        return list(self._string)

    def twist(self):
        for length in self.lengths:
            self._reverse_substring(length)
            self.current_position = (
                self.current_position +
                length +
                self.skip_size
            ) % len(self._string)
            self.skip_size += 1

        return self._string

    def _reverse_substring(self, length):
        self._string.rotate(-self.current_position)
        self._string.extendleft([self._string.popleft() for i in range(length)])
        self._string.rotate(self.current_position)
