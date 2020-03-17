with open("in.txt") as f:
    n = int(f.readline())
    data = f.readlines()
    data = [[int(n) for n in x.split()] for x in data]

even_vertices = []
odd_vertices = []
visited = [False]*n

def is_digraph(graph):
    firstGroup = [0]
    secondGroup = []
    visited[0] = True
    queue = list()
    queue.append(0)
    while (queue):
        v1 = queue.pop(0)
        v2 = get_adj_unvisited_vertex(v1)
        while (v2 != -1):
            if v1 in secondGroup: 
                firstGroup.append(v2)
            else:
                secondGroup.append(v2)
            for j in range(n):
                if (data[v2][j] == 1 and ((v2 in secondGroup and j in secondGroup) 
                or (v2 in firstGroup and j in firstGroup))):
                    return "N"
            visited[v2] = True
            queue.append(v2)
            v2 = get_adj_unvisited_vertex(v1)
    return "Y" + "\n" + ''.join([str(i) for i in firstGroup]) + "0" + "\n" + ''.join(
            [str(i) for i in secondGroup]) + "0" + "\n"

def get_adj_unvisited_vertex(v):
    for j in range(n):
        if data[v][j] == 1 and visited[j] == False:
            return j
    return -1

if __name__ == "__main__":
    f2 = open("out.txt", "w")
    f2.write(is_digraph(data))
