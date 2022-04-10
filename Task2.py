#task2

def minimum_cost(ticket_costs, k):
  min_cost = 0
  for i in range(0,k):
      max1=0
      for j in ticket_costs:
          if j>max1: 
              max1=j
      if len(ticket_costs)!=0: 
         ticket_costs.remove(max1)
  for i in ticket_costs:
      min_cost=min_cost+i
  return min_cost

#ticket_costs = list(map(int, input().split(' ')))
#k = int(input())
#print(minimum_cost(ticket_costs, k))

ticket_costs1=[10, 20, 30, 100, 45]
k1=3
print("First example",minimum_cost(ticket_costs1, k1))
ticket_costs2=[100, 200, 300]
k2=5
print("Second example",minimum_cost(ticket_costs2, k2))
