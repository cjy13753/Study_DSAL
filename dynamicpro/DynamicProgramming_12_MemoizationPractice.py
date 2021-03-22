def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    if count in cache:
        return cache[count]

    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    cache[count] = profit

    return profit

def max_profit_memo_mytry(price_list, count, cache):
    # 코드를 작성하세요.

    if count == 1:
        cache[1] = 100
        return cache[1]

    if count in cache:
        return cache[count]

    temp = []
    for i in range(1, count // 2 + 1):
        temp.append(max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache)) # count가 커지면 temp.append로 인한 메모리 사용 비효율이 너무 커짐

    if count <= 5: # Hard coding해서, price_list의 크기가 변하는 경우 문제가 생길 수 있음
        temp.append(price_list[count])
    
    cache[count] = max(temp)

    return cache[count]
    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))