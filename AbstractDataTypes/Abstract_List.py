# Insert Operation
trending = []

trending.insert(0, "Celeb A")
trending.insert(1, "Concert")
trending.insert(2, "Holidays")
trending.insert(3, "Foods")

print(trending)

trending.insert(1, "Foods")

print(trending)


# Access Operation
print(trending[0])
print(trending[1])

trending[2] = 4

print(trending)

# Search Operation
print("Celeb A" in trending)
print("Celeb B" in trending)

# Delete
del trending[0]

print(trending)