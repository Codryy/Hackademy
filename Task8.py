#Task8

N = int(input())
C=N
M=0
while N:
    M=M*10+N%10
    N=N//10
if M==C: print(C, "is palindrome")
else: print(C, "is not palindrome")
