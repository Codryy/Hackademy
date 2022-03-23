#Task6
#Se citesc două numere naturale - N1 și N2, cu N1 < N2. Să se afișeze pe o singură linie numerele pare dintre ele.

N1 = int(input())
N2 = int(input())
if N1==0: N1=N1+1
for i in range(N1, N2, 1):
    if i%2==0: print(i, end=" ")