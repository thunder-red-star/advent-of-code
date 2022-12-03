# Open the input file
with open('input.txt') as f:
    # Read the input
    lines = f.readlines()

# Initialize a variable to keep track of the total priority
total_priority = 0

# Iterate over the lines in the input
for line in lines:
    # Initialize two sets to keep track of the items in each compartment
    compartment1 = set()
    compartment2 = set()

    # Split the line into two compartments
    comp1, comp2 = line[:len(line) // 2], line[len(line) // 2:]

    # Iterate over the characters in each compartment
    for c in comp1:
        compartment1.add(c)
    for c in comp2:
        compartment2.add(c)

    # Find the common items in each compartment
    common = compartment1.intersection(compartment2)

    # If there is only one common item, add its priority to the total
    if len(common) == 1:
        item = common.pop()
        if item.isalpha():
            if item.islower():
                total_priority += ord(item) - ord('a') + 1
            else:
                total_priority += ord(item) - ord('A') + 27

# Print the total priority
print(total_priority)


# Open the input file
with open('input.txt') as f:
    # Read the input
    lines = f.readlines()

# Initialize a variable to keep track of the total priority
total_priority = 0

# Iterate over the lines in groups of three
for i in range(0, len(lines), 3):
    # Initialize three sets to keep track of the items in each Elf's rucksack
    set1 = set()
    set2 = set()
    set3 = set()

    # Split each line into characters and add them to the appropriate set
    for c in lines[i]:
        set1.add(c)
    for c in lines[i + 1]:
        set2.add(c)
    for c in lines[i + 2]:
        set3.add(c)

    # Find the common items in each rucksack
    common = set1.intersection(set2, set3)

    # If there is only one common item, add its priority to the total
    if len(common) == 1:
        item = common.pop()
        if item.isalpha():
            if item.islower():
                total_priority += ord(item) - ord('a') + 1
            else:
                total_priority += ord(item) - ord('A') + 27

# Print the total priority
print(total_priority)