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


# 3. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-numbers-in-number

number = input()
number_occurences = {}

for length_to_take in range(1, len(number) + 1):
  for starting_position in range(0, len(number)):
    sub_number = number[starting_position:starting_position+length_to_take]
    if sub_number in number_occurences and len(sub_number) == length_to_take:
      number_occurences[sub_number] += 1
    elif len(sub_number) == length_to_take:
      number_occurences[sub_number] = 1
  helpers.find_the_greatest(number_occurences)
  number_occurences = {}

# 4. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-students-scores

number_of_students = input()
subject_grades = {}
students_grades = {}

for _ in range(0, int(number_of_students)):
  student_and_grades = input().split(' ')
  diary = {}
  avg = 0
  for value in student_and_grades[1::]:
    subject, grade = value.split(':')[0], value.split(':')[1]
    if subject in subject_grades:
      subject_grades[subject] = {
        'grade': subject_grades[subject]['grade'] + float(grade),
        'occurences': subject_grades[subject]['occurences'] + 1
      }
    else:
      subject_grades[subject] = {
        'grade': float(grade),
        'occurences': 1
      }
    avg += float(grade)
  avg = avg/(len(student_and_grades) - 1)
  students_grades[student_and_grades[0]] = avg

for student, grade in sorted(students_grades.items()):
  print(student + " " + str(grade))

for subject, avg in sorted(subject_grades.items()):
  print(subject + " " + str(avg['grade']/avg['occurences']))

# 5. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-finding-triangle

number_of_points = int(input())
points = []
for iterator in range(0, number_of_points):
  point = input().split()
  points.append([int(point[0]), int(point[1])])

smallest_area = 0
greatest_area = 0

for iterator in range(1, len(points) + 1):
  first_point = points[iterator - 1]
  for second_point in points[iterator::]:
    for third_point in points[iterator + 1::]:
      area = (abs(first_point[0] * (second_point[1] - third_point[1]) + second_point[0] * (third_point[1] - first_point[1]) + third_point[0] * (first_point[1] - second_point[1])))/2
      if (smallest_area > area and smallest_area != 0 and area != 0) or (smallest_area == 0 and area != 0):
        smallest_area = area
      if area > greatest_area:
        greatest_area = area

print(str(smallest_area) + " " + str(greatest_area))

# 6. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/ppp-test-pionowe-sortowanie

columns, rows = input().split()
matrix = []

# sort

for row in range(0, int(rows)):
  numbers = input().split()
  matrix.append([int(number) for number in numbers])

## TRANSPOSE
matrix = helpers.transpose_matrix_of_vectors(matrix)
## SORT

for row in matrix:
  row.sort()

for column in range(0, int(rows)):
  for row in range(0, int(columns)):
    print(str(matrix[row][column]) + " ", end='')
  print()


# 7. https://www.hackerrank.com/contests/zadania-z-poprzednich-kolokwiow-2223/challenges/pp-test-jumping-in-matrix

FLAG = True
matrix_size = input()
starting_i, starting_j = input().split()
matrix = []

for iterator in range(0, int(matrix_size)):
  numbers = input().split()
  matrix.append([int(number) for number in numbers])

helpers.print_matrix(matrix)

while FLAG:
  # Smallest in row?
  if matrix[int(starting_i)][int(starting_j)] == smallest_in_row(matrix[int(starting_i)]):
    FLAG = False
    break
  # Smallest in column?


def smallest_in_row(matrix):
  min(matrix)
