def matrix_multiply(A, B):
    """Multiplies two 2x2 matrices A and B."""
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def matrix_exponentiation(F, n):
    """Computes matrix exponentiation in O(log n)."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n:
        if n % 2 == 1:
            result = matrix_multiply(result, F)
        F = matrix_multiply(F, F)
        n //= 2
    return result

def fibonacci(n):
    """Returns the nth Fibonacci number using matrix exponentiation in O(log n)."""
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    result = matrix_exponentiation(F, n - 1)
    return result[0][0]

# Example usage
n = int(input("Enter the value of n: "))  # User input
print(f"The {n}th Fibonacci number is:", fibonacci(n))
