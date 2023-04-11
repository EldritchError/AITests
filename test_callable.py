import codon


class PrimeNumbers:
    def is_prime_python(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @codon.jit
    def is_prime_codon(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def __init__(self):
        self.number = 5