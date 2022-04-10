#Task6

N1 = int(input())
N2 = int(input())
if N1==0: N1=N1+1
for i in range(N1, N2, 1):
    if i%2==0: print(i, end=" ")
