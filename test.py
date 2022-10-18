def revers(n):
    x = n//10
    y = n%10
    diff = abs(x-y)
    if x>y:
        return n-(9*diff)
    if x<y:
        return n+(9*diff)
num = int(input("ENTER A TWO DIGHT NUMBER: "))
print(revers(num))