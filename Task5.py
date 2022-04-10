#Task5

N = int(input())

for i in range(0, N+1, 1):
    if i%2==0: print(i*i, end=" ")
    else: print(i*i*i, end=" ")
