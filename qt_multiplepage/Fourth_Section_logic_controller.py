# [ SECTION 4 ] - Logic Part
from Fourth_Section_logic_recipes import Recipes
from Fourth_Section_logic_magic_kitchen import MagicKitchen
from Fourth_Section_logic_open_food_records import FoodRecords, Food 


# This is the class that user interface will call
class LogicController:
    def __init__(self):
        self.recipes         = Recipes()
        self.magic_kitchen   = MagicKitchen()
        self.food_records    = FoodRecords()
    
    def saveFoodRecords(self):

        # step1: random food amount of ingredient for cooking
        number_of_ingredient = self.magic_kitchen.randomNumberOfIngredient()     
        print("step1: number of ingredient", number_of_ingredient,"- pass")

        # step2: get possible menu for cooking from recipes
        possible_menu = self.recipes.getPossibleMenu(number_of_ingredient)
        print("step2: possble menu")
        print(possible_menu)
        print("pass")

        # step3: randomly cook food
        if len(possible_menu) != 0:
            food      = self.magic_kitchen.randomCookMenu(possible_menu)
            food_name = food.getName()
        else:
            food_name = "bug menu"
        print("step3: cook food", "\"" + food_name + "\"","- pass")

        # step4: save the food into the record
        self.food_records.record(food_name)
        print("step4: save record - pass\n\n")



        # return food name so that we can update ui
        return food_name


##############################################
###                                        ###
###  update second_section_ui_main_page    ###
###                                        ###
############################################## TOO....