#Task3

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
