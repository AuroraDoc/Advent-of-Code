numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# I am going to change the strings to string int string so it keeps the letters on both sides
# (eightwo -> eight8eightwo2two)
data = open("day1.txt")
data = data.readlines()


def main():
    total = 0
    for line in data:
        digits = [char for char in translate(line) if char.isdigit()] 
        if digits:
            total += int(digits[0] + digits[-1])
    return total


def translate(line):
    for num, name in enumerate(numbers_list): #makes a list of tuples for the numbers list
        line = line.replace(name, f"{name}{num}{name}") #Replaces the words with wordintword
    return line #returns the line back to the main function where its used


if __name__ == '__main__':
    print(main(total))
