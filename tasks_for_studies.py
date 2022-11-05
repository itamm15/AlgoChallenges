import helpers

# 1. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-find-word-in-matrix

number_of_words, size_of_words = input().split()
WORD_TO_FIND = input()
words = []
state = False

for _ in range(0, int(number_of_words)):
  new_word = input()
  if WORD_TO_FIND in new_word or WORD_TO_FIND in new_word[::-1]:
    print("YES")
    state = True
    break
  else:
    words.append(list(new_word))

# Current representation:
# [
#   [a, a, c]
#   [a, b, c]
#   [a, c, c]
#   [a, b, c]
#   [a, b, c]
# ]
# So the the word occurs also in the martix, column written direction,
# The best idea is going to transpose the 'matrix', and operate on rows.

if not state:
  transposed_matrix = helpers.transpose(words)
  for row in transposed_matrix:
    vertical_word = "".join(row)
    if WORD_TO_FIND in vertical_word or WORD_TO_FIND in vertical_word[::-1]:
      print("YES")
      state = True
      break

# Final check, whether it is not verticaly stored.

if not state:
  print("NO")

# 2. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-linear-independence

matrix_size = input()
vectors = []
state = True
pairs = []
number_of_pairs = 0

for _ in range(0, int(matrix_size)):
  vector = input().split()
  vectors.append(vector)


# Row by row
for row in range(0, len(vectors)):
  for vector in range(row + 1, len(vectors)):
    denominator = (int(vectors[row][0]))
    if denominator != 0:
      r = (int(vectors[vector][0]))/denominator
      for iterator in range(0, int(matrix_size) - 1):
        nominator = (int(vectors[vector][iterator]))
        denominator = int(vectors[row][iterator])
        if denominator != 0 and nominator != 0:
          if nominator/denominator != r:
            state = False
            break
        else:
          if (int(vectors[vector][iterator]) == 0 and int(vectors[row][iterator]) == 0) and not helpers.has_only_zeros(vectors[vector]) and not helpers.has_only_zeros(vectors[row]):
            continue
          else:
            state = False
            break
      if state:
        pairs.append([vectors[vector], [vectors[row]]])
        number_of_pairs += 1
    state = True

# Row by column
transposed_matrix = helpers.transpose_matrix_of_vectors(vectors)

for row in range(0, len(vectors)):
  for vector in range(0, len(vectors)):
    denominator = (int(transposed_matrix[row][0]))
    if denominator != 0:
      r = (int(vectors[vector][0]))/denominator
      for iterator in range(0, int(matrix_size)):
        nominator = (int(vectors[vector][iterator]))
        denominator = (int(transposed_matrix[row][iterator]))
        if denominator != 0 and nominator != 0:
          if nominator/denominator != r:
            state = False
            break
        else:
          if (int(vectors[vector][iterator]) == 0 and int(transposed_matrix[row][iterator]) == 0) and not helpers.has_only_zeros(vectors[vector]) and not helpers.has_only_zeros(transposed_matrix[row]):
            continue
          else:
            state = False
            break
      if state:
        pairs.append([vectors[vector], [transposed_matrix[row]]])
        number_of_pairs += 1
    state = True

# Column by column
for row in range(0, len(vectors)):
  for vector in range(row + 1, len(transposed_matrix)):
    denominator = (int(transposed_matrix[row][0]))
    if denominator != 0:
      r = (int(transposed_matrix[vector][0]))/denominator
      for iterator in range(0, int(matrix_size)):
        nominator = (int(transposed_matrix[vector][iterator]))
        denominator = int(transposed_matrix[row][iterator])
        if denominator != 0 and nominator != 0:
          if nominator/denominator != r:
            state = False
            break
        else:
          if (int(transposed_matrix[vector][iterator]) == 0 and int(transposed_matrix[row][iterator]) == 0) and not helpers.has_only_zeros(transposed_matrix[vector]) and not helpers.has_only_zeros(transposed_matrix[row]):
            continue
          else:
            state = False
            break
      if state:
        pairs.append([transposed_matrix[vector], [transposed_matrix[row]]])
        number_of_pairs += 1
    state = True

print(number_of_pairs)
