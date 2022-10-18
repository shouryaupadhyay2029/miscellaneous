def fibanachi(n):
    if n ==1 or n ==2:
        return 1
    if n ==0:
        return 0
    else:
        return fibanachi(n-1) + fibanachi(n-2)
print(fibanachi(7))