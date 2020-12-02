with open ("input.txt") as f:
    items = []
    for x in f:
        x = x.replace(":", "").replace("\n", "").split(" ")
        items.append(x)

def count_passwd():
    count = 0
    for i in items:
        [min, max] = i[0].split("-")
        letter = i[1]
        q = i[2].count(letter)
        if int(min) <= q and int(max) >= q:
            count += 1
    return count

def main():
    solution = count_passwd()
    print(solution)

if __name__ == "__main__":
    main()