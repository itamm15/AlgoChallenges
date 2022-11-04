def transpose(matrix):
  return [
    [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))
  ]

def print_matrix(matrix):
  for row in matrix:
    print(row)
