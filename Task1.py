#Task 1

def observe_building(heights):
  max_height = 0
  max_distance = 0
  for i in heights:
      if i>max_height:
          max_height=i
          max_distance=heights.index(i)
  return (max_height, max_distance)
heights1=[10, 8, 4, 15, 24, 11]
print("First example",observe_building(heights1))
heights2=[20, 5, 4, 8, 15]
print("Seconds example",observe_building(heights2))
