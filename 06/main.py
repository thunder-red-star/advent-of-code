with open('input.txt') as f:
	lines = f.readlines()

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    # Find the first position where the four most recently received characters are all different
    for i in range(len(line) - 3):
        if len(set(line[i:i+4])) == 4:
            # Report the number of characters from the beginning of the buffer to the end of the first such four-character marker
            print(i + 4)
            break

for line in lines:
    # Find the first position where the 14 most recently received characters are all different
    for i in range(len(line) - 13):
        if len(set(line[i:i+14])) == 14:
            # Report the number of characters from the beginning of the buffer to the end of the first such 14-character marker
            print(i + 14)
            break