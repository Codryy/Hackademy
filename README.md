Online Shopping

With the Black Friday coming up, an online shop of electronics newly established prepared mega discounts and needs help with the logistic of the site. Being at the beginning, the store has a stock made of only two types of products: telephones and refrigerators. Your job is to implement the functionalities necessary to make sure the site runs with no problems.

As example, the shop will have the following functionalities:

User side:

Once an user logs in, he gets an unic customer_id and cand begin his shopping ( login(self, customer_id) );

He can add products in his cart as long as the product is in the stock. An added product will dissapear from the stock ( add_to_cart(self, customer_id, product_name) );

There are situations where the user can change his mind, he does not want to buy a product already in the cart. After a product is eliminated from the cart, he gets restored to the shop stock ( remove_from_cart(self, customer_id, product_name) );

The user can see his products from his cart and their price, and if he is not logged in, return an empty list ( view_cart(self, customer_id) );

In the end, he pays for the products, that means to return the total price of the products in the user's cart, and if the user is not logged in it will return 0         ( checkout(self, customer_id) )

Admin side: Implement a method for the administrator to add products in store stock, double role method, used when the user eliminates from his cart a product           ( add(self,new_product) )

1. Clas Product:

- overloading "+" operator

- returns the sum of the products

2. Class Phone
 
- overloading "str" method

3. Class refrigerator

- overloading "str" method

4. Class Stock

- add a new product in stock

- erase from the store stock the product given as a parameter

- return the current stock

5. Class Cart

- add a product in list_cart

- erase a product from list_cart
 
- calculate sum of products from the cart

- clear the cart after calling the cart_checkout function

6. Class Store

6.1. To do 1:

- add a product in an user's cart with his given id; if the user is not logged in, the operation will not go through

- once a product is added in the cart it will be erased from the store stock

6.2. To do 2:

- erase a product from the user's cart; if the user is not logged in, the operation will not go through

- the product will be added again in the store stock

6.3. To do 3:

- return the list of products from user's cart ( name and price )

6.4. To do 4:

- return the price of the products



