with open ("input.txt") as f:
    items = []
    for x in f:
        items.append(float(x))

def find_values():
    for i, value1 in enumerate(items):
        for j, value2 in enumerate(items):
            for k, value3 in enumerate(items):
                if value1 + value2 + value3 == 2020 and i != j and j != k and k!= i:
                    return value1, value2, value3
    return None

def multiply_values(value1, value2, value3):
    return value1* value2* value3

def main():
    values = find_values()
    if values == None:
        return 0
    v1, v2, v3 = values
    solve = multiply_values(v1, v2, v3)
    print(solve)
    return solve

if __name__ == "__main__":
    main()