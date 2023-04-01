import matplotlib.pyplot as plotter
import numpy as np
import random
import time

#################
#   CONSTANTS   #
#################

a_shaped_data1 = list(range(1, 100, 1)) + list(range(100, 1, -1))
a_shaped_data2 = list(range(1, 110, 1)) + list(range(110, 1, -1))
a_shaped_data3 = list(range(1, 120, 1)) + list(range(120, 1, -1))
a_shaped_data4 = list(range(1, 130, 1)) + list(range(130, 1, -1))
a_shaped_data5 = list(range(1, 140, 1)) + list(range(140, 1, -1))
a_shaped_data6 = list(range(1, 150, 1)) + list(range(150, 1, -1))
a_shaped_data7 = list(range(1, 160, 1)) + list(range(160, 1, -1))
a_shaped_data8 = list(range(1, 170, 1)) + list(range(170, 1, -1))
a_shaped_data9 = list(range(1, 180, 1)) + list(range(180, 1, -1))
a_shaped_data10 = list(range(1, 190, 1)) + list(range(190, 1, -1))
a_shaped_data11 = list(range(1, 200, 1)) + list(range(200, 1, -1))
a_shaped_data12 = list(range(1, 210, 1)) + list(range(210, 1, -1))
a_shaped_data13 = list(range(1, 220, 1)) + list(range(220, 1, -1))
a_shaped_data14 = list(range(1, 230, 1)) + list(range(230, 1, -1))
a_shaped_data15 = list(range(1, 240, 1)) + list(range(240, 1, -1))
a_shaped_data16 = list(range(1, 250, 1)) + list(range(250, 1, -1))
a_shaped_data17 = list(range(1, 260, 1)) + list(range(260, 1, -1))
a_shaped_data18 = list(range(1, 270, 1)) + list(range(270, 1, -1))
a_shaped_data19 = list(range(1, 280, 1)) + list(range(280, 1, -1))
a_shaped_data20 = list(range(1, 290, 1)) + list(range(290, 1, -1))
a_shaped_data21 = list(range(1, 300, 1)) + list(range(300, 1, -1))
a_shaped_data22 = list(range(1, 310, 1)) + list(range(310, 1, -1))
a_shaped_data23 = list(range(1, 320, 1)) + list(range(320, 1, -1))
a_shaped_data24 = list(range(1, 330, 1)) + list(range(330, 1, -1))

data = [
         a_shaped_data1, a_shaped_data2, a_shaped_data3, a_shaped_data4,
         a_shaped_data5, a_shaped_data6, a_shaped_data7, a_shaped_data8,
         a_shaped_data9, a_shaped_data10, a_shaped_data11, a_shaped_data12,
         a_shaped_data13, a_shaped_data14, a_shaped_data15, a_shaped_data16,
         a_shaped_data17, a_shaped_data18, a_shaped_data19, a_shaped_data20,
         a_shaped_data21, a_shaped_data22, a_shaped_data23, a_shaped_data24
       ]

length_of_data = [len(data) for data in data]

################
#  QUICK SORT  #
################

def partition(array, start, end, pivot):
    low = start + 1
    high = end

    while True:
      while low <= high and array[high] >= pivot:
        high = high - 1

      while low <= high and array[low] <= pivot:
        low = low + 1

      if low <= high:
        array[low], array[high] = array[high], array[low]
      else:
        break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, pivot):
  if start >= end:
      return

  part = partition(array, start, end, pivot)
  quick_sort(array, start, part - 1, pivot)
  quick_sort(array, part + 1, end, pivot)


##################
#   EXECUTIONS   #
##################

right_pivot_time = []
middle_pivot_time = []
random_pivot_time = []

for a_shaped_data in data:
  list_length = len(a_shaped_data) - 1
  middle_element = list_length//2
  random_element_within_list_length = random.randint(0, list_length)

  start_time = time.time()
  _right_pivot = quick_sort(a_shaped_data, 0, list_length, a_shaped_data[list_length])
  end_time = time.time()
  right_pivot_time.append(end_time - start_time)

  start_time = time.time()
  _middle_pivot_time = quick_sort(a_shaped_data, 0, list_length, a_shaped_data[middle_element])
  end_time = time.time()
  middle_pivot_time.append(end_time - start_time)

  start_time = time.time()
  _random_pivot_time = quick_sort(a_shaped_data, 0, list_length, a_shaped_data[random_element_within_list_length])
  end_time = time.time()
  random_pivot_time.append(end_time - start_time)

##############
#  PLOTTING  #
##############

_right_pivot = plotter.plot(length_of_data, right_pivot_time, label="Right pivot")
_middle_pivot = plotter.plot(length_of_data, middle_pivot_time, label="Middle pivot")
_random_pivot = plotter.plot(length_of_data, random_pivot_time, label="Random pivot")
plotter.legend()
plotter.xlabel("Array size")
plotter.ylabel("Time")
plotter.show()
