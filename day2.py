aim=0
depth=0
horizontal=0
with open("input.txt") as f:
    for line in f.readlines():
        command=line.split(" ")[0]
        value=int(line.split(" ")[1].strip())
        if (command=="forward"):
            horizontal=horizontal+value
            depth=depth+value*aim
        if (command=="down"):
            aim=aim+value
        if (command=="up"):
            aim=aim-value
print(depth*horizontal)
