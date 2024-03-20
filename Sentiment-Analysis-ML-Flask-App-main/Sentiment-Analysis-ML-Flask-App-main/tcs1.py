import sympy

def find_smallest_prime(input_numbers):
    
    q = min(input_numbers)
    for p in range(q, 10**10):
        if all(p % num == q for num in input_numbers if num != q) and sympy.isprime(p):
            return p
    
    return "None"

input_numbers = list(map(int, input().split()))


result = find_smallest_prime(input_numbers)
print(result)