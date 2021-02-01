'''
 * @file   QuickSort.py
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Armin Zare Zadeh, ali.a.zarezadeh@gmail.com
 * @date   28 Jun 2020
 * @version 0.1
 * @brief   Quick sort implementation
'''

import sys

class QuickSort():
  """
  Mergesort implements InplaceSort for ease of testings, but in reality
  it is not really a good fit for an inplace sorting algorithm.
  """

  def __init__(self):
    pass


  def sort(self, values):
    if values == None: 
      return
    self.quicksort(values, 0, len(values)-1)


  def quicksort(self, ar, lo, hi):
    """
    Sort interval [lo, hi] inplace recursively
    low  --> Starting index,  high  --> Ending index
    https://www.geeksforgeeks.org/quick-sort/
    """
    if lo < hi:
      # pi is partitioning index, ar[pi] is now at right place
      splitPoint = self.partition(ar, lo, hi)
      self.quicksort(ar, lo, splitPoint - 1) # Before pi
      self.quicksort(ar, splitPoint + 1, hi) # After pi


  def partition(self, ar, lo, hi):
    """
    Performs Hoare partition algorithm for quicksort
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot     
    """
    # pivot (Element to be placed at right position)
    pivot = ar[hi] 
 
    i = lo - 1  # Index of smaller element

    for j in range(lo, hi):
      # If current element is smaller than the pivot
      if ar[j] < pivot:
        i += 1  # increment index of smaller element
        self.swap(ar, i, j)

    self.swap(ar, i + 1, hi)
    return i + 1


  def swap(self, ar, i, j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp

#smaller quicksort definition based on the classic haskell implementation
#note: this is quite slow due to list concatenation, but this looks the nicest,
#the time efficiency could be improved by using pythons list.extend method.
def smallsort(arr):
  if len(arr) <= 1: return arr
  else:
    head = arr[0]
    smaller = list(filter(lambda n: n <= head, arr[1:]))
    larger = list(filter(lambda n: n > head, arr[1:]))
    return smallsort(smaller) + [head] + smallsort(larger)

if __name__ == '__main__':
  """
  Example usage
  """
  sorter = QuickSort()
  array = [10, 4, 6, 4, 8, -13, 2, 3]
  sorter.sort(array);
  # Prints:
  # [-13, 2, 3, 4, 4, 6, 8, 10]
  print(array)
