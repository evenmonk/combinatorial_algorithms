with open("in.txt") as f:
    n = int(f.readline())
    data = f.readlines()
    data = [[int(n) for n in x.split()] for x in data]
    s = data[n][0]
    t = data[n + 1][0]
    del data[n]
    del data[n]

prev = [32767]*n
d = [1000000]*n
d[0] = 0

for k in range(1, n):
    for i in range(n):
        for j in range(n):
            if d[j] + data[j][i] < d[i]:
                d[i] = d[j] + data[j][i]
                prev[i] = j

path = []
print(t, prev, prev[t-1])
j = prev[t-1]
path.append(t-1)
print(j)
while j!=32767:
    path.append(j)
    j = prev[j]
path = path[::-1]  

print(d)
print(path)

if d[t-1] == 32767:
    result = "N"
else:
    result = "Y" + "\n" + ' '.join([str(i+1) for i in path]) + "\n" + str(d[t-1])



if __name__ == "__main__":
    f2 = open("out.txt", "w")
    f2.write(result)


