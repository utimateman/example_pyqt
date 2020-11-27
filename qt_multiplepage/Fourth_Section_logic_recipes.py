class Recipes:
    def __init__(self, recipe_file_path='recipes.csv'):
        self.file_path    = recipe_file_path
        self.recipes_list = None

        self.initializeData()
    

    def initializeData(self):

        # open file
        recipes_file = open(self.file_path, 'r')

        # read items in file
        recipes_list = recipes_file.readlines()

        # close file
        recipes_file.close()

        # remove header
        recipes_list.pop(0)

        # manipulating data
        temp = []
        for line in recipes_list:
            line = line.split(',')
            temp.append(line)
        
        self.recipes_list = temp

    def getPossibleMenu(self, number_of_ingredient):

        possible_menu_list = []
        for menu in self.recipes_list:
            if len(menu)-1 == number_of_ingredient:
                possible_menu_list.append(menu)
                
        return possible_menu_list

    
    
