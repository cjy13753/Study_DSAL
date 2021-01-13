stack = [] # deque is also possible and equally efficient

# Insert at the end
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")

# Print the whole stack
print(stack)

# Access the last data in line
print(stack[-1])

# Delete the last data in line
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)