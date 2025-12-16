def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh dibagi nol")
    return a / b
