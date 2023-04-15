import matplotlib.pyplot as plotter
import numpy as np
import random
import time

"""
BST implementation
"""

class BSTNode:
  def __init__(self, value = None):
    self.left = None
    self.right = None
    self.val = value

  """
  Insert
  """

  def insert(self, value):
    if not self.val:
      self.val = value
      return
    if self.val == value:
      return
    if value < self.val:
      if self.left:
        self.left.insert(value)
        return
      self.left = BSTNode(value)
      return

    if self.right:
      self.right.insert(value)
      return
    self.right = BSTNode(value)

  """
  Delete
  """

  def delete(self, value):
    if self == None:
      return self
    if value < self.val:
      self.left = self.left.delete(self, value)
      return self
    if val > self.val:
      self.right = self.right.delete(self, value)
      return self
    if self.right == None:
      return self.left
    if self.left == None:
      return self.right

    min_larger_node = self.right
    while larger_node.left:
      min_larger_node = min_larger_node.left

    self.val = min_larger_node.val
    self.right = self.right.delete(min_larger_node.val)
    return self

  """
  Exists
  """

  def exists(self, value):
    if self.val == value:
      return True
    if self.val > value:
      if self.left == None:
        return False
      return self.left.exists(value)

    if self.right == None:
      return False
    self.right.exists(value)

  """
  Aggregate: Max and min
  """

  def get_min(self):
    current = self
    while current.left is not None:
      current = current.left
    return current.val

  def get_max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current.val

  """
  Printing
  """

  def preorder(self, values):
    if self.val is not None:
      values.append(self.val)
    if self.left is not None:
      self.left.preorder(values)
    if self.right is not None:
      self.right.preorder(values)

    return values

  def inorder(self, values):
    if self.left is not None:
      self.left.inorder(values)
    if self.val is not None:
      values.append(self.val)
    if self.right is not None:
      self.right.inorder(values)

    return values

  def postorder(self, values):
    if self.left is not None:
      self.left.postorder(values)
    if self.right is not None:
      self.right.postorder(values)
    if self.val is not None:
      values.append(self.val)

    return values

  """
  Height
  """

  def height(self):
    leftNodes = 0
    rightNodes = 0
    if self.val == None:
      return '0'
    if self.left is not None:
      leftNodes = self.left.height()
    if self.right is not None:
      rightNodes = self.right.height()

    return max(leftNodes, rightNodes) + 1


"""
AVL tree implementation
"""

class TreeNode(object):
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.height = 1


class AVLTree(object):
  def insert_node(self, root, key):
    if not root:
      return TreeNode(key)
    elif key < root.key:
      root.left = self.insert_node(root.left, key)
    else:
      root.right = self.insert_node(root.right, key)

    root.height = 1 + max(self.get_height(root.left),
                          self.get_height(root.right))

    balanceFactor = self.getBalance(root)
    if balanceFactor > 1:
      if key < root.left.key:
        return self.rightRotate(root)
      else:
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)

    if balanceFactor < -1:
      if key > root.right.key:
        return self.leftRotate(root)
      else:
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)

    return root

  def delete_node(self, root, key):
    if not root:
      return root
    elif key < root.key:
      root.left = self.delete_node(root.left, key)
    elif key > root.key:
      root.right = self.delete_node(root.right, key)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return temp
      temp = self.getMinValueNode(root.right)
      root.key = temp.key
      root.right = self.delete_node(root.right, temp.key)
    if root is None:
      return root

    root.height = 1 + max(self.get_height(root.left),
                          self.get_height(root.right))

    balanceFactor = self.getBalance(root)

    if balanceFactor > 1:
      if self.getBalance(root.left) >= 0:
        return self.rightRotate(root)
      else:
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)
    if balanceFactor < -1:
      if self.getBalance(root.right) <= 0:
        return self.leftRotate(root)
      else:
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)
    return root

  def leftRotate(self, z):
    y = z.right
    if y is not None:
      T2 = y.left
      y.left = z
      z.right = T2
      z.height = 1 + max(self.get_height(z.left),
                          self.get_height(z.right))
      y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))
    return y

  def rightRotate(self, z):
    y = z.left
    if y is not None:
      T3 = y.right
      y.right = z
      z.left = T3
      z.height = 1 + max(self.get_height(z.left),
                          self.get_height(z.right))
      y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))
    return y

  def get_height(self, root):
    if not root:
      return 0
    return root.height

  def getBalance(self, root):
    if not root:
      return 0
    return self.get_height(root.left) - self.get_height(root.right)

  def getMinValueNode(self, root):
    if root is None or root.left is None:
      return root
    return self.getMinValueNode(root.left)

  def preOrder(self, root):
    if not root:
      return
    print("{0} ".format(root.key), end="")
    self.preOrder(root.left)
    self.preOrder(root.right)

"""
MAIN
"""

def main():
  data = [[random.randint(1, 500) for _ in range(20)],
          [random.randint(1, 500) for _ in range(30)],
          [random.randint(1, 500) for _ in range(40)],
          [random.randint(1, 500) for _ in range(50)],
          [random.randint(1, 500) for _ in range(60)],
          [random.randint(1, 500) for _ in range(70)],
          [random.randint(1, 500) for _ in range(80)],
          [random.randint(1, 500) for _ in range(90)],
          [random.randint(1, 500) for _ in range(100)],
          [random.randint(1, 500) for _ in range(110)],
          [random.randint(1, 500) for _ in range(120)],
          [random.randint(1, 500) for _ in range(130)],
          [random.randint(1, 500) for _ in range(140)],
          [random.randint(1, 500) for _ in range(150)],
          [random.randint(1, 500) for _ in range(160)],
          [random.randint(1, 500) for _ in range(170)],
          [random.randint(1, 500) for _ in range(180)],
          [random.randint(1, 500) for _ in range(190)],
          [random.randint(1, 500) for _ in range(210)],
          [random.randint(1, 500) for _ in range(220)],
          [random.randint(1, 500) for _ in range(230)],
          [random.randint(1, 500) for _ in range(240)],
          [random.randint(1, 500) for _ in range(250)],
          [random.randint(1, 500) for _ in range(260)],
          [random.randint(1, 500) for _ in range(270)],
          [random.randint(1, 500) for _ in range(280)],
  ]
  length_of_data = [len(data) for data in data]
  binary_times = []
  binary_heights = []
  avl_times = []
  avl_heights = []

  for numbers in data:
    # GENERATE BINARY TREE
    binary_tree = BSTNode()
    for number in numbers:
      binary_tree.insert(number)

    # GENERATE AVL
    avl_tree = AVLTree()
    root = None
    for number in numbers:
      root = avl_tree.insert_node(root, number)

    # MEASSURE TIME!
    start_time = time.time()
    binary_tree_height = binary_tree.height()
    end_time = time.time()
    binary_times.append(end_time - start_time)
    binary_heights.append(binary_tree_height)

    start_time = time.time()
    avl_tree_height = avl_tree.get_height(root)
    end_time = time.time()
    avl_times.append(end_time - start_time)
    avl_heights.append(avl_tree_height)

    print("Height of binary tree is ", binary_tree_height, ", and AVL tree is ", avl_tree_height, "\n")

  # PLOTTING

  # _binary_tree_time = plotter.plot(length_of_data, binary_times, label="Binary tree")
  # _avl_tree_time = plotter.plot(length_of_data, avl_times, label="AVL tree")
  _binary_tree_height = plotter.plot(length_of_data, binary_heights, label="Binary tree")
  _avl_tree_height = plotter.plot(length_of_data, avl_heights, label="AVL tree")
  plotter.legend()
  plotter.xlabel("Tree size")
  plotter.ylabel("Height")
  plotter.show()

main()
