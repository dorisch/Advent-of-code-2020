with open ("input.txt") as f:
    items = []
    for x in f:
        x = x.replace("\n", "")
        items.append(x)

def get_new_list():
    length_items = len(items)
    new_list = []
    for i in items:
        new_list.append(i*length_items)
    return new_list

def count_trees(trajectory_list):
    trees = 0
    n = 0
    for r, t in enumerate(trajectory_list):
        if t[n] == '#':
            trees += 1
        n += 3
    return trees

def main():
    trajectory_list = get_new_list()
    solution = count_trees(trajectory_list)
    print(solution)

if __name__ == "__main__":
    main()