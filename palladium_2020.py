# What is the minimum total area of at most two banners which cover all of the
# buildings?
# 
# Write a function:
# 
#     def solution(H)
# 
# that, given an array H consisting of N integers, returns the minimum total area
# of at most two banners that we will have to order.

def comp_max(H, i0, i1):
    m = H[i0]
    for i in range(i0,i1+1):
        m = max(m, H[i])
    return m

def solution(H):
    area_min = comp_max(H,0,len(H)-1) * len(H)
    for i in range(0, len(H) - 1):
        max_left = comp_max(H,0,i)
        max_right = comp_max(H,i+1,len(H)-1)
        area = max_left * (i + 1) + max_right * (len(H) - i - 1)
        area_min = min(area, area_min)
    return area_min

H = [3, 1, 4]
if solution(H) == 10:
	print ("Test A: OK")
else:
	print ("Test A: Error")

H = [5, 3, 2, 4]
if solution(H) == 17:
	print ("Test A: OK")
else:
	print ("Test A: Error")

H = [5, 3, 5, 2, 1]
if solution(H) == 19:
	print ("Test A: OK")
else:
	print ("Test A: Error")

H = [7, 7, 3, 7, 7]
if solution(H) == 35:
	print ("Test A: OK")
else:
	print ("Test A: Error")

H = [1, 1, 7, 6, 6, 6]
if solution(H) == 30:
	print ("Test A: OK")
else:
	print ("Test A: Error")
