# Find the numbers adjacent to symbols even diagonally.
# Idea: Make a coordinate system. Assign each symbol a coordinate. Then check if there are digits on any of the
#       Bordering coordinates
# ** Idea2: use the coordinate system but when it hits either a digit or a symbol it checks if the other is around and then
#           adds it if the other is touching

# Steps:
#   1) find out what special chars are used
#   2) assign chars that arent "." a cord
#   3) Check the surroundings and assign if it is or isnt part num
#   4) add or dont add to total
# Simplest identifiers come last. Symbols are always one char but
#
# scan
# if a symbol is found scan around each cord for an int
# parsing out numbers, join it to string then convert to int
# steps now:
# - record data
# - cast string to int
# - reset vals
#- sum up results array

class Cords:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def has_symbol(self, data):
        is_symbol = False
        left = self.x - 1
        right = self.x + 1
        up = self.y - 1
        down = self.y + 1

        left_most = self.__check_symbol((self.y, left), data) #this passes in the direction tuple
        if left_most != '.' and not left_most.isdigit():
            is_symbol = True
        up_left = self.__check_symbol((up, left), data)
        if up_left != '.' and not up_left.isdigit():
            is_symbol = True
        up_most = self.__check_symbol((up, self.x), data)
        if up_most != '.' and not up_most.isdigit():
            is_symbol = True
        up_right = self.__check_symbol((up, right), data)
        if up_right != '.' and not up_right.isdigit():
            is_symbol = True
        right_most = self.__check_symbol((self.y, right), data)
        if right_most != '.' and not right_most.isdigit():
            is_symbol = True
        down_right = self.__check_symbol((down, right), data)
        if down_right != '.' and not down_right.isdigit():
            is_symbol = True
        down_most = self.__check_symbol((down, self.x), data)
        if down_most != '.' and not down_most.isdigit():
            is_symbol = True
        down_left = self.__check_symbol((down, left), data)
        if down_left != '.' and not down_left.isdigit():
            is_symbol = True

        return is_symbol

    def __check_symbol(self, direction: tuple, data: list):
        if direction[0] < 0 or direction[1] < 0:
            return '.'
        try:
            character = data[direction[0]][direction[1]]
            return character
        except IndexError:
            return "."

    def __str__(self): #overrides returning mem address, this returns what you want\
        return f"{self.x}, {self.y} ({self.char})"




def main():
    with open("day3.txt", "r") as data:  # data is a list not a string
        data = [line.replace("\n", "") for line in data]
        part_nums = []
        for y, line in enumerate(data):
            arr = []
            is_part_num = False
            for x, char in enumerate(line):
                if char.isdigit():
                    cord = Cords(x, y, char) #initializes data
                    if cord.has_symbol(data): #if it has a symbol
                        is_part_num = True #this shits a part num
                    arr.append(cord)  # creates a class object for each number
                elif arr:
                    new_num = int("".join([cord.char for cord in arr]))
                    if is_part_num:
                        part_nums.append(new_num)
                    is_part_num = False
                    arr = []
            print(sum(part_nums))


if __name__ == '__main__':
    main()