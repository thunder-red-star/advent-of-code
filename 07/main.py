with open('input.txt') as f:
    lines = f.readlines()

i = 0
current_dir = None
directories = {}
subdirectories = {}


def join(*args):
    return '/'.join(args)


def normalize_path(path):
    path = path.split('/')
    newpath = []
    for i in path:
        if i == '..':
            newpath.pop()
        elif i != '.':
            newpath.append(i)
    return '/'.join(newpath)


def directory_size(dirname):
    dsize = directories[dirname]
    for i in subdirectories[dirname]:
        if i in directories:
            dsize += directory_size(i)
    return dsize


for line in lines:
    if len(line.strip()) == 0:
        continue
    if line[0] == '$':
        command, *args = line.split()[1:]
        if command == 'cd':
            path, = args
            if path[0] == '/':
                current_dir = path
            else:
                current_dir = normalize_path(join(current_dir, path))
            if current_dir not in directories:
                directories[current_dir] = 0
                subdirectories[current_dir] = []
    else:
        size, filename = line.split()
        if size != 'dir':
            directories[current_dir] += int(size)
        else:
            subdirectories[current_dir].append(normalize_path(join(current_dir, filename)))


# part 1
dirsizes = {}
total_size = 0
for directory in directories:
    dir_size = directory_size(directory)
    if dir_size <= 100000:
        total_size += dir_size
print(total_size)

# part 2
total_size = directory_size('/')
unused = 70000000 - total_size
dir_size = 0
max_size = None
for directory in directories:
    dir_size = directory_size(directory)
    if unused + dir_size >= 30000000:
        if max_size is None or max_size > dir_size:
            max_size = dir_size
print(max_size)

# i could have imported os lmao
