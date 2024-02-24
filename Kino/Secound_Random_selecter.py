import random

# Take user input for list of numbers
numbers = []
while True:
    num = input("Enter a number (or type 'done' to finish): ")
    if num.lower() == "done":
        break
    numbers.append(int(num))

# Take user input for group size
group_size = int(input("Enter the group size: "))

# Divide the numbers into groups
groups = []
while len(numbers) >= group_size:
    group = random.sample(numbers, group_size)
    groups.append(group)
    for number in group:
        numbers.remove(number)

# Print the groups
for group in groups:
    print(group)
