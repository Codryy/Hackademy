#Task 2
#Scrieți un program care sa scrie @nydailybugle.com în loc de @gmail.com.

mail=input("Introdu mail sa te furam: ")

if '@gmail.com' in mail:
    mail = mail.replace('gmail.com', 'nydailybugle.com')
print(mail)
