#Task 2

mail=input("Please write your email ")

if '@gmail.com' in mail:
    mail = mail.replace('gmail.com', 'nydailybugle.com')
print(mail)
