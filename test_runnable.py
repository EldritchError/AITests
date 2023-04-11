import test_callable
from time import time

PrimenumberOperator = test_callable.PrimeNumbers()

t0 = time()
ans = sum(1 for i in range(100000, 200000) if PrimenumberOperator.is_prime_python(i))
t1 = time()
print(f'[python] {ans} | took {t1 - t0} seconds')

t0 = time()
ans = sum(1 for i in range(100000, 200000) if PrimenumberOperator.is_prime_codon(i))
t1 = time()
print(f'[codon] {ans} | took {t1 - t0} seconds')