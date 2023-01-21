import math
import numpy
import sympy
import random
import time
import matplotlib.pyplot as plotter

# ------------------------------------------ #
# The algorithm is working for matrix sizes.
# ------------------------------------------ #

# --------------------- #
# For size = 2          #
# [                     #
#   [a, b],             #
#   [c, d]              #
# ]                     #
# The determinant is:   #
#  a*d - c*b            #
# --------------------- #

# --------------------- #
# For size = 3          #
# [                     #
#  [a, b, c],           #
#  [d, e, f],           #
#  [g, h, i]            #
# ]                     #
# The determinant is    #
# more complex.         #
# a*det([[e,f],[h,i]])  #
# b*det([[d,f],[g,i]])  #
# c*det([[d.e],[g,h]])  #
# --------------------- #

def generate_random_matrix(matrix_size):
  temporary_matrix = []
  for _ in range(0, int(matrix_size)):
    new_matrix = [random.randint(0, 10) for _ in range(0, int(matrix_size))]
    temporary_matrix.append(new_matrix)

  return temporary_matrix

def calculate_the_determinant(matrix):
  if len(matrix) == 1:
    return matrix[0][0]
  if len(matrix) == 2:
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
  if len(matrix) >= 3:
    ### Let's stick with first row
    sum = 0
    for iterator in range(0, len(matrix)):
      ### Delete row
      temp_matrix = numpy.delete(matrix[:], 0, 0)
      ### Delete column
      temp_matrix = numpy.delete(temp_matrix, int(iterator), 1)
      sum_of_determinant = matrix[0][int(iterator)] * calculate_the_determinant(temp_matrix)
      if iterator % 2 == 0:
        sum += sum_of_determinant
      else:
        sum -= sum_of_determinant
    return sum

##### NUMPY #####

matrix_size = input()
matrix = generate_random_matrix(int(matrix_size))

numpy_time_start = time.time()
numpy_result = numpy.linalg.det(matrix)
numpy_time_finish = time.time()

##### SYMPY #####

sympy_matrix = sympy.Matrix(matrix)
sympy_time_start = time.time()
sympy_result = sympy_matrix.det()
sympy_time_fisnih = time.time()

##### OWN #####

own_time_start = time.time()
own_result = calculate_the_determinant(matrix)
own_time_finish = time.time()

##### RESULTS #####

print("NUMPY: ", numpy_result)
print("SYMPY: ", sympy_result)
print("OWN: ", own_result)

##### DISPLAY RESULTS #####

print("Time complexity of numpy: ", numpy_time_finish - numpy_time_start)
print("Time complexity of sympy: ", sympy_time_fisnih - sympy_time_start)
print("Time complexity of own algo: ", own_time_finish - own_time_start)

##### PLOTING #####

# Calculate
values = [1, 2, 3, 4, 5, 6, 7, 8]
num = []
sym = []
own = []

for value in values:
  matrix = generate_random_matrix(value)
  ## num
  numpy_time_start = time.time()
  numpy_result = numpy.linalg.det(matrix)
  numpy_time_finish = time.time()
  num.append(numpy_time_finish - numpy_time_start)
  ## sym
  sympy_matrix = sympy.Matrix(matrix)
  sympy_time_start = time.time()
  sympy_result = sympy_matrix.det()
  sympy_time_fisnih = time.time()
  sym.append(sympy_time_fisnih - sympy_time_start)
  ## own
  own_time_start = time.time()
  own_result = calculate_the_determinant(matrix)
  own_time_finish = time.time()
  own.append(own_time_finish - own_time_start)

plotter.plot(values, num, label="Num")
plotter.plot(values, sym, label="Sym")
plotter.plot(values, own, label="Own")
plotter.legend()
plotter.show()
