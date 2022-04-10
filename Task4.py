#Task4

N = int(input())
for i in range(0, N, 1):
  x=input()
  y=input()
  t=input()
  x = int(x)
  y = int(y)
  if(t == 'i'):
    print(x//y, end=" ")
  if(t == 'f'):
    print(x/y, end=" ")
  if(t == 'p'):
    print(x**y, end=" ")
