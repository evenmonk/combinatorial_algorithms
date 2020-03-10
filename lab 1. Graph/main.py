with open("input.txt") as f:
    n = int(f.read(1))
    data = f.readlines()
    del data[0]
    data = [[int(n) for n in x.split()] for x in data]
 
def is_digraph(graph):
    # пустой инициализатор заполняет массив нулями
    even_vertices = []
    odd_vertices = []
    marks = [0]*n
    for i in range(n):
        # для каждой вершины
        for j in range(n):
            # перебираем её соседей
            if graph[i][j]:
                # если j-ая вершина соседняя
                if ((marks[i] % 2) == (marks[j] % 2) and marks[j]):
                    # и если чётность совпадает с текущей и уже пройдена, 
                    # то граф не двудольный
                    return "N"
                else:
                    # иначе установим чётность вершины 
                    marks[j] = marks[i] + 1
    # пробежали все вершины

    for x in range(n):
        if marks[x] % 2 == 0:
            even_vertices.append(x+1)
        else:
            odd_vertices.append(x+1)

    if even_vertices[0] < odd_vertices[0]:
        return "Y" + "\n" + ' '.join([str(i) for i in even_vertices]) + "\n" + "0" + "\n" + ' '.join([str(i) for i in odd_vertices])
    else:
        return "Y" + "\n" + ' '.join([str(i) for i in odd_vertices]) + "\n" + "0" + "\n" + ' '.join([str(i) for i in even_vertices])


if __name__ == "__main__":
    f2 = open("output.txt", "w")
    f2.write(is_digraph(data))
