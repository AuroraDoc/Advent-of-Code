# you get a list of numbers split with a |
# first set is winning numbers second set is numbers that you have.
# first match is 1 point and then each match after doubles
# separate into two lists of winning nums and your nums, loop through it and if any match append to a third list
# len of matches list
# to count the points just use 1 * 2**len

total = 0
with open("day4,1.txt", "r") as data:
    for line in data:
        num = line.split(':')
        nums = num[1].split('|')

        matches = []
        winning_nums = list(nums[0].split())
        elfs_nums = list(nums[1].split())

        for val in elfs_nums:
            if val in winning_nums:
                matches.append(val)

        num_of_matches = len(matches)
        if num_of_matches == 0:
            continue
        else:
            points = 2 ** (num_of_matches - 1)

        total += points
        print(total)