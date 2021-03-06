# -*- coding: utf-8 -*-
"""1-Sricharan Yedu Thirnathi.ipynb
"""

# Python program of Insertion Sort

def insertion_sort(A):
  n = len(A)
  for j in range(1,n):
    key = A[j]
    i = j-1
    while i>=0 and A[i]>key:
      A[i+1] = A[i]
      i = i-1
      A[i+1] = key

A = [5,2,4,6,1,3]

insertion_sort(A)
print("The array after implementation of Insertion Sort is:", A)

# Python program for Merge sort

import math

def merge_sort(A,p,r):

  if p<r:

    q = (p+r) // 2
    merge_sort(A,p,q)
    merge_sort(A,q+1,r)
    merge(A,p,q,r)

def merge(A,p,q,r):
  
  n1 = q-p+1
  n2 = r-q

  L = [0]*(n1+1)
  R = [0]*(n2+1)

  for i in range(0, n1):
    L[i] = A[p+i]
  for j in range(0, n2):
    R[j] = A[q+j+1]

  L[n1] = math.inf
  R[n2] = math.inf

  i = 0
  j = 0

  for k in range(p, r+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i+1
    
    else:
      A[k] = R[j]
      j = j+1

array = [5,2,4,7,1,3,2,6]

merge_sort(array, 0 , len(array)-1)

print("The array after implementation of Merge Sort is:", array)
