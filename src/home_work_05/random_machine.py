import random
from typing import List

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    
    for i in range(2, int(x * 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

def primes(count: int) -> List[int]:
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def checksum(x: List[int]) -> int:
    ini_sum = 0
    for i in x:
        ini_sum = ini_sum + i
        ini_sum = ini_sum * 113
        ini_sum = ini_sum % 10000007
    
    return ini_sum

def pipeline() -> int:
    primes_list = primes(1000)
    random.seed(100)
    random.shuffle(primes_list)
    res = checksum(primes_list)
    return res

if __name__ == "__main__":
    print(pipeline())