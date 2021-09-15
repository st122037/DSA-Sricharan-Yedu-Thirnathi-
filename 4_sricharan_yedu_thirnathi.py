# -*- coding: utf-8 -*-
"""4-Sricharan Yedu Thirnathi.ipynb
"""

#Heapsort

def Left(i):
  return i*2 + 1

def Right(i):
  return i*2 

def Max_Heapify(A, i, heap_size): 
    l = Left(i)
    r = Right(i)
    if l <= heap_size and A[l] > A[i]:
       largest = l
    else: 
      largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest, heap_size)

def Build_Max_Heap(A, heap_size):
  for i in range(heap_size//2, 0, -1):
    Max_Heapify(A, i, heap_size)

def HeapSort(A, heap_size):
  Build_Max_Heap(A, heap_size)
  for i in range(heap_size, 0, -1):
    A[0], A[i] = A[i], A[0]
    heap_size = heap_size - 1
    Max_Heapify(A, 0, heap_size)

A = [45, 4, 10, 14, 7, 9,]
#heap_size = len(A[1:])
#HeapSort(A, heap_size)
#print(A[0:])   
HeapSort(A,len(A)-1)
print(A)





#QuickSort

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]

    A[i+1],A[r] = A[r],A[i+1]
    return i+1


A = [12,34,5,-20,1]
quicksort(A, 0, len(A)-1)
print(A)
