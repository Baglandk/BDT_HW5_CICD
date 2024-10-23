from src.home_work_05.random_machine import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(-3) == False
    assert is_prime(3) == True
    assert is_prime(17) == True

def test_primes():
    assert primes(2) == [2, 3]

def test_checksum():
    assert checksum([1, 2, 6, 24]) == 6012369

def test_pipline():
    assert pipeline() == 7785816

if __name__ == "__main__":
    test_is_prime()
    test_primes()
    test_checksum()
    test_pipline()