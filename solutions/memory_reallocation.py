class Reallocator:
    def __init__(self, banks=None):
        self.banks = banks or list(range(16))
        self.history = []
        self.current_index = 0

    def reallocate(self):
        largest_bank = self._get_largest_bank()
        memory_to_distribute = self.banks[largest_bank]
        self._advance_to_largest_bank(largest_bank)
        self._redistribute(largest_bank, memory_to_distribute)
        self._remember_state()

    def actively_reallocate(self):
        while 1:
            self.reallocate()
            if self._has_repeated_state():
                return len(self.history)

    def _has_repeated_state(self):
        return self.history[-1] in self.history[:-1]

    def _get_largest_bank(self):
        highest = 0
        for i in range(len(self.banks)):
            if self.banks[highest] < self.banks[i]:
                highest = i
        return highest

    def _advance_to_largest_bank(self, largest_bank):
        self.current_index = largest_bank

    def _redistribute(self, largest_bank, memory_to_distribute):
        self.banks[largest_bank] = 0  # empty current largest bank
        for _ in range(memory_to_distribute):
            next_index = ((self.current_index + 1) % len(self.banks))
            self.banks[next_index] += 1
            self.current_index += 1

    def _remember_state(self):
        self.history.append(self.banks[:])
