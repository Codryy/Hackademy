#Task5
#Fie o listă de parole formate din numere sau litere. Să se valideze fiecare parolă după următoarele criterii:
#lungime minimă de 8 caractere
#cel puțin o cifră
#cel puțin un caracter majusculă
#Se va returna lista de parole invalide.

def password_validation(password_list):

  invalid_passwords = []
  b=int(0)
  c=int(0)
  for i in password_list:
      b=0
      c=0
      for j in i:
         if j>="A" and j<="Z":
            b=b+1
      for k in i:
          if k>="0" and k<="9":
              c=c+1
      if len(i)<8 or b==0 or c==0:
          invalid_passwords.append(i)
  return invalid_passwords
# DO NOT MODIFY
password_list = list(map(str, input().split(' ')))
print(password_validation(password_list))