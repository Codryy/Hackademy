#Task5

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
password_list=["test", "gdf6sdAvf", "nacsSDsdf", "lungime2FG", "faracifreG", "faramajuscula2", "faracifresimajuscule", "sfg2hGfbghH5645AAbfghbg", "asd54hcfdgF", "bfgv8", "AAAAAA", "7bvnrgr657H4bhg"]
print(password_validation(password_list))
