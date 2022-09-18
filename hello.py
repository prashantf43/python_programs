d1 = {"a":200, "b":300, "c":100}
d2 = {"a":300, "b":100, "d":400}
d3 = {}

for x in d1:
    if x in d2:
        d3[x]=d1[x]+d2[x]
    else:
        print(d1[x])
        d3[x]=d1[x]

for x in d2:
    if x not in d3:
        d3[x]=d2[x]
print(d3)