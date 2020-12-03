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

def count_trees(trajectory_list, right, down):
    trees = 0
    n = 0
    for r, t in enumerate(trajectory_list):
        if down == 2 and r%2==1:
            continue
        if t[n] == '#':
            trees += 1
        n += right
    return trees

def main():
    trajectory_list = get_new_list()
    solution1 = count_trees(trajectory_list, 1 , 1)
    solution2 = count_trees(trajectory_list, 3 , 1)
    solution3 = count_trees(trajectory_list, 5 , 1)
    solution4 = count_trees(trajectory_list, 7 , 1)
    solution5 = count_trees(trajectory_list, 1 , 2)
    print(solution1*solution2*solution3*solution4*solution5)

if __name__ == "__main__":
    main()