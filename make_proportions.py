A4_H = 297
A4_W = 210
with open("allowable_proportions.txt", "w") as f:
    for ycount in range(11, 16 + 1):
        for xcount in range(8, 11 + 1):
            f.write(f"{A4_H/ycount}:{A4_W/xcount}\n")
