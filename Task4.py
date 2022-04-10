#Task4
#Ca developer TikTok, ai fost rugat să identifici prietenii comuni ai utilizatorilor pentru a îmbunătăți faimosul lor algoritm de sugestie. 
#Pentru asta, va trebui să completezi funcția get_common_friends ce primește ca parametri listele de prieteni ale celor două persoane și întoarce o listă ce conține prietenii lor comuni, sortați lexicografic. Dacă cele două persoane nu au niciun prieten în comun, lista va conține doar string-ul None.
#BONUS: completează funcția get_different_friends ce returnează o listă cu prietenii diferiți dintre cele două persoane (sortați ca mai devreme). 
#Dacă cele două persoane nu au niciun prieten diferit, lista va conține string-ul None.

def get_common_friends(friends1, friends2):
  common = []
  s1=set()
  s2=set()
  a=set()
  for i in friends1:
      s1.add(i)
  for i in friends2:
      s2.add(i)
  a=s1.intersection(s2)
  for i in a:
      common.append(i)
  common.sort()
  if len(common)==0:
      common.append("None")
  return common
  

def get_different_friends(friends1, friends2):
  different = []
  s3=set()
  s4=set()
  b=set()
  c=set()
  for i in friends1:
      s3.add(i)
  for i in friends2:
      s4.add(i)
  b=s3.difference(s4)
  c=s4.difference(s3)
  for i in b:
      different.append(i)
  for i in c:
      different.append(i)
  different.sort()
  if len(different)==0:
      different.append("None")
  return different
  

# DO NOT MODIFY
friends1 = list(input().split(' '))
friends2 = list(input().split(' '))
print(get_common_friends(friends1, friends2))
print(get_different_friends(friends1, friends2))