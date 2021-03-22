def consecutive_sum(start, end):
    # 코드를 작성하세요
    if start == end:
        return start
    else:
        new_start1 = start
        new_end1 = (start + end) // 2
        new_start2 = new_end1 + 1
        new_end2 = end
        return consecutive_sum(new_start1, new_end1) + consecutive_sum(new_start2, new_end2)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))