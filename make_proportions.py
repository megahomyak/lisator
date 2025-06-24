A4_H = 297
A4_W = 210
a = []
with open("allowable_proportions.txt", "w") as f:
    for ycount in range(11, 16 + 1):
        for xcount in range(8, 11 + 1):
            a.append((ycount, xcount, (A4_H/ycount) / (A4_W/xcount)))
            print(ycount, xcount, (A4_H/ycount) / (A4_W/xcount))
            #f.write(f"{A4_H/ycount}:{A4_W/xcount}\n")
print(len(set(a)))
print(len(a))
