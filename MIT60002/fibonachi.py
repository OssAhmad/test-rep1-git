def fibo(x): 
    if x == 0:
        return 0
    if x == 1: 
        return 1 + 0
    if x > 1:
        return fibo(x-1) + fibo(x-2)
memo = {}
def fastFibo(x):
    if x == 0 or x == 1:
        memo[x] = 1
        return memo[x]
    else: 
        memo[x] = memo[x-1] + memo[x-2]
        return memo[x]

for i in range(1000):
    print("fib("+str(i)+") is this:", fastFibo(i))
# print(memo)