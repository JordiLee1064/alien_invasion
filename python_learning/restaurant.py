class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is: ", self.restaurant_name)
        print("Cuisine type is: ", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

my_restaurant = Restaurant("全聚德", "豫菜")
# my_restaurant.describe_restaurant()
# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)
# my_restaurant.open_restaurant()
print(my_restaurant.number_served)
my_restaurant.set_number_served(500)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(50)
print(my_restaurant.number_served)
