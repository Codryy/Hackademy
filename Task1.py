#Task 1
#Se citește o listă de numere naturale reprezentând înălțimile unor blocuri. 
#Un observator se află pe prima clădire din listă și privește în față, blocurile sunt așezate la o distanță de o unitate.
# Completând funcția observe_buildings, să se întoarcă înălțimea ultimului bloc pe care acesta îl vede și distanța până la el sub formă de tuplu.
#În cazul în care nu există nicio clădire mai înaltă decât cea pe care se află observatorul, se va întoarce înălțimea acesteia și 0.

def observe_building(heights):
  max_height = 0
  max_distance = 0
  # TODO
  for i in heights:
      if i>max_height:
          max_height=i
          max_distance=heights.index(i)
  return (max_height, max_distance) 
# DO NOT MODIFY
heights = list(map(int, input().split(' ')))
print(observe_building(heights))