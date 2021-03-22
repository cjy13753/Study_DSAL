def min_fee(pages_to_print):
    # 코드를 작성하세요. 
    sorted_list = sorted(pages_to_print)

    sum = 0

    for i in range(len(sorted_list)):
        sum += sorted_list[i] * (len(sorted_list) - i)

    return sum



def min_fee_kernel(pages_to_print):
    if len(pages_to_print) < 2:
        return pages_to_print[0]

    return pages_to_print[0] * len(pages_to_print) + min_fee(pages_to_print[1:])

def min_fee_mytry(pages_to_print):
    # 코드를 작성하세요. 

    pages_to_print.sort(reverse=False)
    return min_fee_kernel(pages_to_print) 
    



# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
