with open ("input.txt") as f:
    items = []
    for x in f:
        items.append(float(x))

def find_values():
    for i, value1 in enumerate(items):
        for j, value2 in enumerate(items):
            if value1 + value2 == 2020 and i != j :
                return value1, value2

def multiply_values(value1, value2):
    return value1* value2

def main():
    v1, v2 = find_values()
    solve = multiply_values(v1, v2)
    print(solve)

if __name__ == "__main__":
    main()