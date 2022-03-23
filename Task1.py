#Task 1
#Citiți de la tastatură numărul de credite al fiecărei materii (numere întregi), apoi aflați și afișați totalul punctelor de credit.

sum = 0
for i in range(4):
    credite=int(input("Introduceti credite: "))
    sum = sum + credite
print(sum)


