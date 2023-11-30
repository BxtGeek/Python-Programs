with open ("file/name.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} age is {row[1]}")