adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

adjacency_matrix[0] = [0, 1, 1, 0, 0, 0]
adjacency_matrix[1] = [1, 0, 0, 1, 0, 1]
adjacency_matrix[2] = [1, 0, 0, 0, 0, 1]
adjacency_matrix[3] = [0, 1, 0, 0, 1, 1]
adjacency_matrix[4] = [0, 0, 0, 1, 0, 1]
adjacency_matrix[5] = [0, 1, 1, 1, 1, 0]


print(adjacency_matrix)