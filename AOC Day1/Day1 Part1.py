data = open("day1.txt", "r")
data = data.readlines() #so now we have a list of the data
list_total = []
total = 0

for line in data:
    nums = [num for num in line if num.isdigit()]
    #keep doing stuff to the individual lists until we get the two digit numbers we want
    two_nums = []
    if len(nums) > 1:
        two_nums.append(nums[0])
        two_nums.append(nums[-1])
    else:
        two_nums.append(nums[0])
        two_nums.append(nums[0])

    joined_nums = ["".join(two_nums)]
    final_nums = [int(digits) for digits in joined_nums]
    list_total.append(final_nums[0]) #appends the value. if you dont do the first index its another list inside

for i in list_total:
    total += i

print(total)





