#Task 1

It is read a list of natural numbers representing the height of buildings. An observer stands on the first building of the list and looks forward. The buildings are at a distance of one. Write the function observe_buildings that returns the heigth of the last bulding he sees and the distance to it. The result must be a tuple. If there are not any buildings higher that the one the observer sits on, the output will consist of the height of the observer's building and 0.

Exemple 1:

Input: heights=[10, 8, 4, 15, 24, 11]

Output: max_height=24 max_distance=4

Exemple 2:

Input: heights=[100, 8, 3]

Output: max_height=100 max_distance=0

#Task 2

There is a list that contains natural numbers that represents the cost of a cinema ticket and a number of vouchers k. A voucher offers an 100% discount for every type of ticket. Write the function minimum_cost that returs the minimum a client can spend after applying the k vouchers.

Exemple:

Input: ticket_costs=[23, 41, 28, 16, 50] k=2

Output: min_cost=67

#Task 3

It is read a natural number that represents the number of movies that received ratings from different internet sites. The rating statistics is represented in the form of a dictionary in which the keys are the movie names. The values are represented by a list that contains integer numbers for movie ratings. We define rating global of a film as the rating average of a movie. Write the global_ratings function which returns a dictionary with the keys as movie names and values as the global rating of every movie.

Exemple:

Input:

ratings = {
'Bonnie and Clyde' : [8, 9, 10],
'Inception' : [6, 8, 7]
}

Output:

global_ratings = {
'Bonnie and Clyde' : 9,
'Inception' : 7
}

#Task 4

As a TikTok developer, you were asked to identify the common friends of users to improve the faimous algorith system. For this, you will need to write the get_common_friends function that receives as parameters lists of friends of the two persons and returns a list that contains the common friends, sorted lexicographical. If the persons don't have any common friends, the list will only contain the string "None".

Bonus: Complete the function get_different_friends that returns a lists with the different friends of the two users ( sorted as above ). If the persons don't have any different friends, the list will contain the string "None"

Exemple:

Input:

friends1 = ['Ana', 'Maria', 'Florin', 'Mihai', 'George', 'Ioana', 'Tudor']

friends2 = ['Florin', 'Laura', 'Oana', 'Paul', 'Tudor', 'Ana']

Output:

common = ['Ana', 'Florin', 'Tudor']

Bonus:

different = ['George', 'Ioana', 'Laura', 'Maria', 'Mihai', 'Oana', 'Paul']

#Tesk 5

There is a list with passwords formed of numbers and letters. Write a program that validates every passwords according to the next criterias:

A max length of 8 characters
A minimum of one number
A minimum of one uppercase character
It will return the list of invalid passwords

Exemple:

Input:

password_list = ['alEg0Bb1', 'lAl834dc', 'ILpfd38', 'anaaremere']

Output:

invalid_passwords = ['ILpfd38', 'anaaremere']

Explaining: the password ILpfd38 has less than 8 characters and the passwords anaaremere does not have any special character of number.



