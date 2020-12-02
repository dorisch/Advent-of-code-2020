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
        letters_list = list(i[2])
        j = int(min) - 1
        k = int(max) - 1
        
        if letters_list[j] == letter and letters_list[k] == letter:
            continue
        elif letters_list[j] == letter or letters_list[k] == letter:
            count += 1
    return count

def main():
    solution = count_passwd()
    print(solution)

if __name__ == "__main__":
    main()