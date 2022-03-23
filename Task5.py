#Task5
#Se citește de la tastatură un număr întreg pozitiv N. 
#Pentru toate numerele întregi i ce fac parte din intervalul [0, N], să se afișeze pătratul lui i, dacă acesta este număr par
# In caz contrar să se afișeze cubul. Rezultatele trebuie pe o singură linie.

N = int(input())

for i in range(0, N+1, 1):
    if i%2==0: print(i*i, end=" ")
    else: print(i*i*i, end=" ")
