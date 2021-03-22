def max_profit(price_list, count):
    # 코드를 작성하세요.
    profit_table = [0]

    for i in range(1, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]

def max_profit_mytry(price_list, count):
    # 코드를 작성하세요.

    cache = {}
    
    cache[0] = price_list[0]
    cache[1] = price_list[1]

    if count < 2:
        return cache[count]

    for i in range(2,count + 1):
        if count < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, cache[i - j] + cache[j])
        
        cache[i] = profit

    return cache[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
