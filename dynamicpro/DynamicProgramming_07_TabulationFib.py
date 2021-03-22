def fib_tab(n):
    # 코드를 작성하세요.
    fib_table = [0, 1, 1]

    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]

def fib_tab_mytry(n):
    # 코드를 작성하세요.
    if n < 3:
        return n

    cache = {1: 1, 2: 1}

    for i in range(1, n-1):
         cache[i+2] = cache[i] + cache[i+1]

    return cache[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
