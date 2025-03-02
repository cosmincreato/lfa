def read():
    with open("input.txt") as f:
        global term, neterm, start, n, dir
        dir = {}
        neterm = [val for val in f.readline().strip().split()]
        term = [val for val in f.readline().strip().split()]
        start = f.readline().strip()
        n = int(f.readline().strip())
        for line in f.readlines():
            st, dr = line.strip().split(" -> ")
            dir[st] = [x for x in dr.split(" | ")]


queue = []
ans = []
read()

for val in dir[start]:
    queue.append(val)

while queue:
    word = queue.pop(0)
    last = word[-1]
    # daca ultima lit e neterm (litera mare)
    if last.isupper():
        crt = word[:-1]
        for val in dir[last]:
            new = crt + val
            if len(new) <= (n+1):
                queue.append(crt + val)
    # daca ultima lit e term (litera mica) sau lambda (.)
    else:
        if last == '.':
            word = word[:-1]
        if len(word) == n:
            ans.append(word)

print(f"{len(ans)} cuvinte generate")

with open("output.txt","w") as f:
    for val in ans:
        f.write(val+'\n')