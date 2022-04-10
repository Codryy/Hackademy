#Task4

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

friends1=['Ana', 'Maria', 'Florin', 'Mihai', 'George', 'Ioana', 'Tudor']
friends2=['Florin', 'Laura', 'Oana', 'Paul', 'Tudor', 'Ana']
print(get_common_friends(friends1, friends2))
print(get_different_friends(friends1, friends2))
