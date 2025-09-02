import numpy as np

class SpiralBrain:
    def __init__(self, n_max=10**6):
        self.n_max = n_max
        self.shells = self.generate_shells()

    def generate_shells(self):
        primes = self.prime_sieve(self.n_max)
        theta = 2 * np.pi * np.log(primes) / np.log(self.n_max)
        shells = [{'n': int(p), 'theta': float(t)} for p, t in zip(primes, theta)]
        return shells

    def prime_sieve(self, limit):
        sieve = np.ones(limit + 1, dtype=bool)
        sieve[:2] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                sieve[i*i::i] = False
        return np.flatnonzero(sieve)