#Task9

N = int(input())
fib1=0
fib2=1
for i in range(0, N, 1):
    fib1=fib1+fib2
    fib2=fib1-fib2
print(fib1)
