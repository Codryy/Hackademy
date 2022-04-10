#Task3
#Se citeste un număr natural ce reprezintă numărul de filme care au primit rating pe diverse site-uri de pe internet. 
#Statistica rating-urilor este reprezentată în forma unui dicționar în care cheile reprezintă numele fimelor.
#Valorile sunt reprezentate de câte o listă ce conține numere întregi pentru rating-urile filmului.
#Definim rating global al unui film ca fiind media tuturor rating-urilor. 
#Completați funcția global_ratings care va întoarce un dicționar ce are ca și cheie numele filmelor, iar valorile reprezintă rating-ul global al fiecăruia.

def global_ratings(ratings):
    global_ratings = dict()
    for key,Value in rating.items():
          c=0
          for i in Value:
                c+=i
          medie=c/len(Value)
    global_ratings[key]=medie
    return global_ratings
 
number_movies = int(input())
ratings = dict()

for _ in range(number_movies):
    line = input().split(" ")
    movie = line[0]
    current_ratings = []
    for rating in line[1:]:
        current_rating = int(rating)
        current_ratings.append(current_rating)
    ratings[movie] = current_ratings

print(global_ratings(ratings))