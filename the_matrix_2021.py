# You are given an N × N matrix in which every cell is colored black or white.
# Columns are numbered from 0 to N-1 (from left to right). This coloring is
# represented by a non-empty array of integers A. If the K-th number in the array
# is equal to X then the X lowest cells in the K-th column of the matrix are
# black. The rest of the cells in the K-th column are white. The task is to
# calculate the side length of the biggest black square (a square containing only
# black cells).
# 
# Write a function:
# 
#     def solution(A)
# 
# that, given an array of integers A of length N representing the coloring of the
# matrix, returns the side length of the biggest black square.

def is_square(A,i0,i1):
    height = i1 - i0 + 1
    for i in range(i0, i1 + 1):
        if A[i] < height:
            return False
    return True

def calc_max_square(A,i0):
    i = i0
    while i < len(A) and is_square(A, i0, i):
        i += 1
    return i - i0


def solution(A):
    biggest = 0
    for i in range(len(A)):
        area = calc_max_square(A,i)
        biggest = max(biggest, area)
    return biggest
    

A = [1, 2, 5, 3, 1, 3]

if solution(A) == 2:
	print ("Test A: OK")
else:
	print ("Test A: Error")

A = [3, 3, 3, 5, 4]

if solution(A) == 3:
	print ("Test A: OK")
else:
	print ("Test A: Error")

A = [6, 5, 5, 6, 2, 2]

if solution(A) == 4:
	print ("Test A: OK")
else:
	print ("Test A: Error")
