def bubble_sort(array):
  """冒泡排序"""
  n = len(array)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array
