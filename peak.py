import numpy as np

# 1D linear search
def find_peak(list):
        for n in range(0,len(list)-1):
            if list[n] >= list[n-1] and list[n] >= list[n+1]:
                return n

list = [8, 9, 0, 12, 5, 6]
x = find_peak(list)
print('From linear peak finding',list[x])

#1D binary search
def binary_peak_search(list):
    left = 0
    right = len(list)-1
    mid = (left+right)//2
    if list[mid] > list[mid-1]:
        list = list[:mid]
    else:
        list = list[mid:]
    for n in range(0,len(list)-1):
        if list[n] >= list[n-1] and list[n] >= list[n+1]:
            return n
y = binary_peak_search(list)
print('From binary peak search',list[y])


#2d peak
import numpy as np

z = np.array([[1,2,3],
              [8,6,4],
              [1,5,3]])
peak = []
for x in range(0,3):
    for y in range(0,3):