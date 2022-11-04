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
