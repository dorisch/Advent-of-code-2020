data = {(x.split("contain")[0])[:-1].replace(" bags", "").replace(" bag", ""): (x.split("contain")[1]).split(",") for x in open("input.txt").read().split("\n")}
keys = {}
keys_list = []

for k,v in data.items():
    keys[k] = 0

keys_list = ["shiny gold"]
keys["shiny gold"] = 1
score = 0

score = 0
for key in keys_list:
    c = keys[key]
    if c != 0:
        values = data[key]
        sum = 0
        for v in values:
            v_list = v.split(" ")[1:]
            k = v_list[1] + " " + v_list[2]
            if v_list[0] != 'no':
                sum += int(v_list[0])
                keys[k] = int(v_list[0])*c
                keys_list.append(k)
        score += sum*c


print(score)
