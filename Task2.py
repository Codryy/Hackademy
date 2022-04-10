#task2
#Fie o listă de numere naturale ce reprezintă costul unui bilet la cinematograf și un număr k de vouchere. 
#Un voucher oferă o reducere de 100% pentru orice tip de bilet.
#Să se completeze funcția minimum_cost ce returnează costul minim ce poate fi obținut după aplicarea a k vouchere.

def minimum_cost(ticket_costs, k):
  min_cost = 0
  max2=0
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
ticket_costs = list(map(int, input().split(' ')))
k = int(input())
print(minimum_cost(ticket_costs, k))