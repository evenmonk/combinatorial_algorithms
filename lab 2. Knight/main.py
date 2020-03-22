with open("in.txt") as f:
    first_line = f.readline()
    second_line = f.readline()

knight_position = [ord(first_line[0]) - 97, int(first_line[1]) - 1]
pawn_position = [ord(second_line[0]) - 97, int(second_line[1]) - 1]
adjacency_matrix = [[0 for x in range(64)] for x in range(64)]
visited_vertex = [False for x in range(64)]
   
def get_adjacency_priority(first_position, second_position) :
    if ((first_position[0] + 1 == second_position[0]) and (first_position[1] + 2 == second_position[1])): return 8
    if ((first_position[0] - 1 == second_position[0]) and (first_position[1] + 2 == second_position[1])): return 7
    if ((first_position[0] - 2 == second_position[0]) and (first_position[1] + 1 == second_position[1])): return 6
    if ((first_position[0] - 2 == second_position[0]) and (first_position[1] - 1 == second_position[1])): return 5
    if ((first_position[0] - 1 == second_position[0]) and (first_position[1] - 2 == second_position[1])): return 4
    if ((first_position[0] + 1 == second_position[0]) and (first_position[1] - 2 == second_position[1])): return 3
    if ((first_position[0] + 2 == second_position[0]) and (first_position[1] - 1 == second_position[1])): return 2
    if ((first_position[0] + 2 == second_position[0]) and (first_position[1] + 1 == second_position[1])): return 1
    else: return 0


def convert_number_to_position(n):
    return [int(n/8), int(n%8)]

def convert_position_to_number(n):
    return n[0] * 8 + n[1]

# building adjacency matrix
for i in range(64):
    current_position = convert_number_to_position(i)
    for j in range(64):
        adjacent_position = convert_number_to_position(j)
        adjacency_matrix[i][j] = get_adjacency_priority(current_position, adjacent_position)

def get_adjacent_unvisited_vertex(n):
    lst = []
    for j in range(64):
        lst.append(adjacency_matrix[n][j])
    while (visited_vertex[lst.index(max(lst))] and max(lst) != 0):
        lst[lst.index(max(lst))] = 0
    if (max(lst) == 0): return -1
    return lst.index(max(lst))

def vertex_to_string(n):
    position = convert_number_to_position(n)
    return chr(position[0] + 97) + str(position[1] + 1) + "\n"

def dfs(knight_position, pawn_position):
    numerical_knight_position = convert_position_to_number(knight_position)
    numerical_pawn_position = convert_position_to_number(pawn_position)
    visited_vertex[numerical_knight_position] = True
    stack = []
    f2 = open("out.txt", "w")


    # pawn is able to kill knight
    if(numerical_pawn_position % 8 != 0):
        if (numerical_pawn_position <= 55):
            visited_vertex[numerical_pawn_position + 7] = True
        if (numerical_pawn_position >= 9):
            visited_vertex[numerical_pawn_position - 9] = True
    
    f2.write(vertex_to_string(numerical_knight_position))
    stack.append(numerical_knight_position)

    while (stack):
        v = get_adjacent_unvisited_vertex(stack[-1])
        print(v, stack[-1], "adjvertex")
        if (v == -1): stack.pop()
        else:
            visited_vertex[v] = True
            f2.write(vertex_to_string(v))
            if (v == numerical_pawn_position): break
            stack.append(v)

dfs(knight_position, pawn_position)

