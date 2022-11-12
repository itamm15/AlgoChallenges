def transpose(matrix):
  return [
    [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))
  ]

def transpose_matrix_of_vectors(matrix):
  return list(map(list, zip(*matrix)))

def print_matrix(matrix):
  for row in matrix:
    print(row)

def has_only_zeros(matrix):
  all(int(index) == 0 for index in matrix)

def find_the_greatest(numbers):
  number, occurences = int(list(numbers.keys())[0]), list(numbers.values())[0]
  for key, value in list(numbers.items())[1::]:
    if value > occurences:
      number = int(key)
      occurences = value
    elif value == occurences and int(key) < number:
      number = int(key)
  print(number)
