
# Simple in-memory cache dictionaries
_pow_cache = {}
_fibonacci_cache = {}
_factorial_cache = {}

def pow_operation(base: float, exponent: float) -> float:
    key = (base, exponent)
    if key in _pow_cache:
        return _pow_cache[key]
    result = base ** exponent
    _pow_cache[key] = result
    return result

def fibonacci_operation(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")
    if n in _fibonacci_cache:
        return _fibonacci_cache[n]
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    _fibonacci_cache[n] = a
    return a

def factorial_operation(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in _factorial_cache:
        return _factorial_cache[n]
    result = 1
    for i in range(2, n + 1):
        result *= i
    _factorial_cache[n] = result
    return result
