memo =[]
for i in range(1000):
    memo.append(-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(12))


#bottom_up 



"""def fib(n, memo):
    if memo[n] is (no,memo) + fib(n-2,memo):
        memo[n] = result
    return result"""
    
def fib_memo(n):
    if n == 1 or n ==2:
        return 1
    bottom_up = [None]*(n+1)
    bottom_up[1] = 1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
print(fib(12))
