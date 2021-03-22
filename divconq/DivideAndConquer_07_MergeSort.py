
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.9f} seconds")

def mergesort_mytry(my_list):
    def merge(a, b):
        new = []
        while len(a) > 0 or len(b) > 0:
            if len(a) == 0 and len(b) > 0:
                new.append(b.pop(0))
            elif len(a) > 0 and len(b) == 0:
                new.append(a.pop(0))
            elif len(a) > 0 and len(b) > 0:
                if a[0] >= b[0]:
                    new.append(b.pop(0))
                else:
                    new.append(a.pop(0))

        return new

    if len(my_list) <= 2:
        new_list1 = my_list[:len(my_list)//2]
        new_list2 = my_list[len(my_list)//2:]

    else:
        new_list1 = mergesort_mytry(my_list[:len(my_list)//2])
        new_list2 = mergesort_mytry(my_list[len(my_list)//2:])
    
    return merge(new_list1, new_list2)

# 테스트
t = Timer()
t.start()
print(mergesort_mytry([1, 3, 5, 7, 9, 11, 13, 11]))
t.stop()

t.start()
print(mergesort_mytry([28, 13, 9, 30, 1, 48, 5, 7, 15]))
t.stop()

t.start()
print(mergesort_mytry([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
t.stop()

def mergesort(my_list):
    def merge(list1, list2):
        merged_list = []

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                merged_list.append(list2[j])
                j += 1
            else:
                merged_list.append(list1[i])
                i += 1

        if i == len(list1):
            merged_list += list2[j:]

        elif j == len(list2):
            merged_list += list1[i:]

        return merged_list

    if len(my_list) < 2:
        return my_list
    
    left_half = my_list[:len(my_list) // 2]
    right_half = my_list[len(my_list)//2:]

    return merge(mergesort(left_half), mergesort(right_half))

# 테스트
t.start()
print(mergesort([1, 3, 5, 7, 9, 11, 13, 11]))
t.stop()

t.start()
print(mergesort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
t.stop()

t.start()
print(mergesort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
t.stop()


