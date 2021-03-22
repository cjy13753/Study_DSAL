def fib_optimized(n):
    # 코드를 작성하세요.
    current = 1
    previous = 0

    for i in range(1, n):
        current, previous = current + previous, current
    
    return current


def fib_optimized_mytry(n):
    # 코드를 작성하세요.

    previous = 1
    current = 1

    if n < 3:
        return current

    for i in range(1, n-1):
        temp = current
        current = previous + current
        previous = temp

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
