data = {(x.split("contain")[0])[:-1].replace("bags", "").replace("bag", ""): (x.split("contain")[1]).split(",") for x in open("input.txt").read().split("\n")}
print(data)

keys = ["shiny gold"]

for key in keys:
    for k, v in data.items():
        for i in v:
            if key in i and k not in keys:
                keys.append(k)
                break
 
k = set(keys)
print(len(k)-1)
