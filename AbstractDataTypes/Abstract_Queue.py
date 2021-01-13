# Queue in Python is deque(Doubly-ended-queue)
from collections import deque

queue = deque()

# Append Operation
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")
queue.append("E")

print(queue)

# Access Operation
print(queue[0])

# Popleft operation
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)