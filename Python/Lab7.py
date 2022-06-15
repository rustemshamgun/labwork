rows = []
while True:
    row = input()
    if row=="":
        break
    rows.append(row)

l = [[int(x) for x in a.split() if int(x)%2==0] for a in rows]
print(l)