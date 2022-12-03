with open('input.txt') as f:
    lines = f.readlines()

# Create an empty list to store each Elf's inventory
inventories = []
current_inventory = []

# Iterate over the lines of input
for line in lines:
    # If the line is empty, this is the end of an Elf's inventory
    if not line.strip():
        # Add the current Elf's inventory to the list of inventories
        inventories.append(current_inventory)
        # Reset the current inventory to an empty list
        current_inventory = []
    else:
        # This line is a food item, so add it to the current inventory
        current_inventory.append(int(line))

# Sum the calories in each sublist to find the total calories carried by each Elf
elf_calories = [sum(inventory) for inventory in inventories]

# Find the maximum number of calories carried by an Elf
max_calories = max(elf_calories)

# Print the maximum number of calories carried by an Elf
print(max_calories)

# Create an empty list to store each Elf's inventory
inventories = []
current_inventory = []

# Iterate over the lines of input
for line in lines:
    # If the line is empty, this is the end of an Elf's inventory
    if not line.strip():
        # Add the current Elf's inventory to the list of inventories
        inventories.append(current_inventory)
        # Reset the current inventory to an empty list
        current_inventory = []
    else:
        # This line is a food item, so add it to the current inventory
        current_inventory.append(int(line))

# Sum the calories in each sublist to find the total calories carried by each Elf
elf_calories = [sum(inventory) for inventory in inventories]

# Sort the Elves by the number of calories they are carrying, in descending order
elf_calories.sort(reverse=True)

# Sum the calories carried by the top three Elves
total_calories = sum(elf_calories[:3])

# Print the total number of calories carried by the top three Elves
print(total_calories)
