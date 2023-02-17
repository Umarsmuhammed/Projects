#Chapter 9: Classes
#Exercise 9-1.Restaurant: Make a class called Restaurant. The __init__() method 
# for Restaurant that store two attributes: a restaurant_name and a cuisine_type. 
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Meena and Tribes", "Kano")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Exercise 9-2. Three Restaurants:  Create three different instances from the class, 
# and call describe_restaurant() for each instance
Restaurant_1 = Restaurant('Shab\'an','Special')
Restaurant_2 = Restaurant('Arabian suite','Masa')
Restaurant_3 = Restaurant('Gusto','foreign dishes')
print(Restaurant_1.describe_restaurant())
print(Restaurant_2.describe_restaurant())
print(Restaurant_3.describe_restaurant())

#Exercise 9-3.Users: Make a class called User, Create two attributes 
# called first_name and last_name
class User:
    def __init__(self,first_name,last_name,age,school,course_of_study,city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school = school
        self.city = city
        self.course_of_study = course_of_study
        
    def describe_user(self):
        print(f'{self.first_name} {self.last_name}, am {self.age} years old,study at  {self.school}, read {self.course_of_study}')
    def greet_user(self):
        print(f'Good day {self.first_name} {self.last_name}, how are you doing')
user_1 = User('Umar','Sani',30,'M Sc Mathematics','BUK', 'kano')
user_2 = User('Ammar','Muhammad',29,'B Sc Electrical Engineering','KUST', 'Wudil')
user_3 = User('Zainab','Adam',23,'HIM','SHT', 'Kano')
print(f'Greeting user one: {user_1.describe_user()}')
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

#Exercise 9-4.Number Served:Add an attribute called number_served 
# with a default value of 0.
class Restaurant_2:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f'{self.restaurant_name} offers the best {self.cuisine_type} meals and has served {self.number_served} customers so far')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open, food is now ready')
    def set_number_served(self,num):
        '''Set the number of customers that have been served'''
        if num >= self.number_served:
            self.number_served = num
        else:
            print('We enjoy the food!!')
    def increment_number_served(self,add):
        '''Increase the number of customers served by an amount'''
        if add > 0:
            self.number_served += add
        else:
            print('Customers served can\'t be reduced')

restaurant = Restaurant_2('MamaTee','Italian')
restaurant.number_served   # 0
restaurant.number_served = 3
restaurant.describe_restaurant() 
restaurant.set_number_served(15)
restaurant.describe_restaurant()  
restaurant.increment_number_served(5)
restaurant.describe_restaurant()  

#Exercise 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
#  Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
class User_2:
    def __init__(self,first_name,last_name,age,city,course_of_study,school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.course_of_study = course_of_study
        self.school = school
        self.login_attempts = 0


    def describe_user(self):
        '''Print user profile'''
        print(f'{self.first_name} {self.last_name}, a {self.age} years old {self.course_of_study} lives in {self.city}')
    def greet_user(self):
        print(f'Good day {self.first_name} {self.last_name}, how is your day')    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user_ex = User_2('Umar','Sani',30,'M Sc Mathematics','BUK', 'kano')
user_ex.increment_login_attempts()  # called it multiple times
print(user_ex.login_attempts) #23
user_ex.reset_login_attempts()
print(user_ex.login_attempts)  # back to zero

#Exercise 9-6.Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','strawberry']
    def display_flavors(self):
        print(f'\nWe have the follwing icecream flavors')
        for item in self.flavors:
            print(f'-{item}')
rose = IceCreamStand('Biggies','French')
rose.display_flavors()

#Exercise 9-7.Admin:

#Exercise 9-8.Privileges:

#Exercise 9-9.Battery Upgrade: Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). This method 
#should check the battery size and set the capacity to 100 if it isn’t already. 
#Make an electric car with a default battery size, call get_range() once, and 
#then call get_range() a second time after upgrading the battery. You should 
#see an increase in the car’s range.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"The car covers {self.odometer_reading} miles per hour.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('smooth ride an odometer')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        '''Upgrade the battery if there's a need'''
        if self.battery_size == 75:
            self.battery_size = 100
            print('Battery has been upgraded to 100KWh')
        else:
            print('Battery already upgraded')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nChecking the range after upgrading battery:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#Exercise 9-10:Imported Restaurant

#Exercise 9-11:Imported Admin

#Exercise 9-12:

#Exercise 9-13:
'''Make a class Die with one attribute called sides, which has a default 
value of 6. Write a method called roll_die() that prints a random number 
between 1 and the number of sides the die has. Make a 6-sided die and roll it 
10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''
import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

# Create a 6-sided die and roll it 10 times
d6 = Die()
for i in range(10):
    d6.roll_die()

# Create a 10-sided die and roll it 10 times
d10 = Die(sides=10)
for i in range(10):
    d10.roll_die()

# Create a 20-sided die and roll it 10 times
d20 = Die(sides=20)
for i in range(10):
    d20.roll_die()

#Exercise 9-14:Lottery
''': Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message saying
that any ticket matching these four numbers or letters wins a prize'''
# define a list of 10 numbers and 5 letters
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
# randomly select four items from the list
winning_items = random.sample(my_list, 8)
# print a message announcing the winning items
print(f"Congratulations! Any ticket matching the following four items wins a prize: {winning_items}")

#Exercise 9-15:Lottery Analysis
''' You can use a loop to see how hard it might be to win the kind of lottery you
just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling
numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket'''
# Define the pool of possible numbers and letters
pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [2, 4, 'X', 'Y']

# Initialize a counter to keep track of how many times the loop runs
counter = 0

# Keep pulling numbers until your ticket wins
while True:
    # Randomly select four items from the pool
    winning_ticket = random.sample(pool, 4)
    
    # Check if the winning ticket matches your ticket
    if winning_ticket == my_ticket:
        print(f"Congratulations! You won the lottery after {counter} tries!")
        break
    
    # Increment the counter
    counter += 1

##Exercise 9-16:Python Module of the Week
''' One excellent resource for exploring the Python standard library is a site
called Python Module of the Week. Go to https://pymotw.com/ and look at the table
of contents. Find a module that looks interesting to you and read about it, 
perhaps starting with the randommodule.
Styling Classes
A few styling issues related to classes are worth clarifying, especially as your 
programs become more complicate'''


