# [ SECTION 4 ] - Logic Part
from Fourth_Section_logic_open_food_records import Food 

# for random
import random

class MagicKitchen:
    def __init__(self):
        self.food    = None

    def randomNumberOfIngredient(self):
        # random number
        random_result = random.randint(2,3) # random 2 and 3
        return random_result

    def randomCookMenu(self, possible_menu):
        # choose menu
        number_of_possible_menu = len(possible_menu) 
        random_menu_index = random.randint(0, number_of_possible_menu - 1) 

        food = self.cook(possible_menu[random_menu_index][0]) # possible_menu : [ [fried rice, egg, rice ] , [ egg salad, egg, vegetable] ]
        return food

    def cook(self, menu_name):
        # just make it looks cleaner(?)
        food = Food(menu_name)
        return food


