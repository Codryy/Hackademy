#Task4
#Se citește de la tastatură un număr N, si apoi N triplete de forma x y t. Să se afișeze pe o singură linie, în funcție de t, următoarele:
#t = 'i' -> rezultatul împărțirii lui x la y ca numere întregi
#t = 'f' -> rezultatul împărțirii lui x la y ca numere reale
#t = 'p' -> rezultatul ridicării lui x la puterea y

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
