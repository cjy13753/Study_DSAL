def swap_elements(mylist, a, b):
    temp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = temp

def partition(mylist, start, end):
    i = start
    s = start
    p = end

    while i != end:
        if mylist[i] >= mylist[p]:
            swap_elements(mylist, i, s)
            s += 1
        i += 1
    
    swap_elements(mylist, s, p)
    p = s

    return p
    

def quicksort(mylist, start=0, end=None):
    if end is None:
        end = len(mylist) - 1
    
    if len(mylist[start:end + 1]) < 2:
        return

    p = partition(mylist, start, end)
    
    quicksort(mylist, start, p - 1)
    quicksort(mylist, p + 1, end)

def merge(list1, list2):
    index1 = 0
    index2 = 0

    len_list1 = len(list1)
    len_list2 = len(list2)

    merged_list = []

    while (index1 != len_list1) or (index2 != len_list2):
        if index1 != len_list1 and index2 != len_list2:
            if list1[index1] >= list2[index2]:
                merged_list.append(list1[index1])
                index1 += 1
            else:
                merged_list.append(list2[index2])
                index2 += 1
        elif index1 != len_list1 and index2 == len_list2:
            merged_list.append(list1[index1])
            index1 += 1
        elif index1 == len_list1 and index2 != len_list2:
            merged_list.append(list2[index2])
            index2 += 1
    
    return merged_list

def mergesort(unsorted_list):
    
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    return merge(mergesort(unsorted_list[:len(unsorted_list) // 2]), mergesort(unsorted_list[len(unsorted_list) // 2:]))

def min_coin_count_quicksort(value, coin_list):
    # 코드를 작성하세요.
    
    chains = {}
    quicksort(coin_list)

    for i in range(len(coin_list)):
        temp = 0
        while value - coin_list[i] >= 0:
            temp += 1
            chains[coin_list[i]] = temp
            value -= coin_list[i]

    return chains, sum(list(chains.values()))

def min_coin_count_mergesort(value, coin_list):
# 코드를 작성하세요.

    chains = {}
    coin_list = mergesort(coin_list)

    for i in range(len(coin_list)):
        temp = 0
        while value - coin_list[i] >= 0:
            temp += 1
            chains[coin_list[i]] = temp
            value -= coin_list[i]

    return chains, sum(list(chains.values()))

def min_coin_count_guide(value, coin_list):
    count = 0

    for coin in sorted(coin_list, reverse=True):
        count += (value // coin)

        value %= coin

    return count


# 테스트
print("Guide")
default_coin_list = [100, 500, 10, 50]
print(min_coin_count_guide(1440, default_coin_list))
print(min_coin_count_guide(1700, default_coin_list))
print(min_coin_count_guide(23520, default_coin_list))
print(min_coin_count_guide(32590, default_coin_list))

print("")

default_coin_list = [100, 500, 10, 50]
print("Quicksort")
print(min_coin_count_quicksort(1440, default_coin_list))
print(min_coin_count_quicksort(1700, default_coin_list))
print(min_coin_count_quicksort(23520, default_coin_list))
print(min_coin_count_quicksort(32590, default_coin_list))

print("")

print("Mergesort")
default_coin_list = [100, 500, 10, 50]
print(min_coin_count_mergesort(1440, default_coin_list))
print(min_coin_count_mergesort(1700, default_coin_list))
print(min_coin_count_mergesort(23520, default_coin_list))
print(min_coin_count_mergesort(32590, default_coin_list))

a = [1, 3, 2, 5]
a.sort(reverse=True)
print(a)