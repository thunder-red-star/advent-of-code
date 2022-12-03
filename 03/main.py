with open('input.txt') as f:
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

    # For each common item, add its priority to the total
    for item in common:
        if item.isalpha():
            if item.islower():
                total_priority += ord(item) - ord('a') + 1
            else:
                total_priority += ord(item) - ord('A') + 27

# Print the total priority
print(total_priority)

# Initialize a variable to keep track of the total priority
total_priority = 0

# Iterate over the lines in the input
for i in range(0, len(lines), 3):
    # Initialize two sets to keep track of the items in each compartment
    compartment1 = set(lines[i])
    compartment2 = set(lines[i + 1])
    compartment3 = set(lines[i + 2])

    # Find the common items in each compartment
    common = set.intersection(compartment1, compartment2, compartment3)

    # For each common item, add its priority to the total
    for item in common:
        if item.isalpha():
            if item.islower():
                total_priority += ord(item) - ord('a') + 1
            else:
                total_priority += ord(item) - ord('A') + 27

# Print the total priority
print(total_priority)