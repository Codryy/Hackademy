#Task8
#Dându-se un număr natural N, scrieți un program care să verifice dacă acesta este sau nu palindrom și afișați un mesaj corespunzător ("N este palindrom" sau "N nu este palindrom").

N = int(input())
C=N
M=0
while N:
    M=M*10+N%10
    N=N//10
if M==C: print(C, "este palindrom")
else: print(C, "nu este palindrom")