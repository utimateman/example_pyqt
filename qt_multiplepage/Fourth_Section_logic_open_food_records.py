# [ SECTION 4 ] - Logic Part


class FoodRecords:
    def __init__(self, record_file_path='my_food_record.txt'):
        self.file_path = record_file_path

    def record(self, food_name):
        write_file = open(self.file_path,'a')
        write_file.write(food_name + "\n")
        write_file.close()


class Food:
    def __init__(self, name):
        self.name = name

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name