with open('input.txt') as f:
    lines = f.readlines()

assignments = []

# For each line
for line in lines:
    # Split by comma
    line = line.split(',')
    # Add tuple of both items to assignments
    assignments.append((line[0], line[1].strip()))

# Initialize a counter
counter = 0

# Iterate over each pair of assignments
for (a1, a2) in assignments:
  # Split the assignments into start and end range
  (start1, end1) = a1.split("-")
  (start2, end2) = a2.split("-")

  # Convert the ranges to integers
  start1 = int(start1)
  end1 = int(end1)
  start2 = int(start2)
  end2 = int(end2)

  # Check if one range fully contains the other
  if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
    # Increment the counter
    counter += 1

# Print the result
print(counter)

counter = 0

for (a1, a2) in assignments:
  # Split the assignments into start and end range
  (start1, end1) = a1.split("-")
  (start2, end2) = a2.split("-")

  # Convert the ranges to integers
  start1 = int(start1)
  end1 = int(end1)
  start2 = int(start2)
  end2 = int(end2)

  # Check if the ranges overlap
  if (start1 <= end2 and end1 >= start2) or (start2 <= end1 and end2 >= start1):
    # Increment the counter
    counter += 1

# Print the result
print(counter)