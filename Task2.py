#Task 2

mail=input("Introdu mail sa te furam: ")

if '@gmail.com' in mail:
    mail = mail.replace('gmail.com', 'nydailybugle.com')
print(mail)
