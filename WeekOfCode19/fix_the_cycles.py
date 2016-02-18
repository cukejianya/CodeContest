def find_min_path(array):
    path_1 = node_A(array, 0, "A", False)
    path_2 = node_B(array, 0, "B", False)

    minimum = min(path_1, path_2)

    if minimum < 0:
        ans = abs(minimum)
    else:
        ans = 0

    return ans

def node_A(array, weight, first_node, cleared):
    if cleared and first_node == "A":
        return weight
    cleared = True
    path_1 = node_B(array, weight+array[1], first_node, cleared)
    if  first_node == "A":
        path_2 = node_C(array, weight+array[4], first_node, cleared)
    else:
        path_2 = path_1

    return min(path_2, path_1)

def node_B(array, weight, first_node, cleared):
    if cleared and first_node == "B":
        return weight
    cleared = True
    path_1 = node_C(array, weight+array[2], first_node, cleared)
    path_2 = node_D(array, weight+array[5], first_node, cleared)

    return min(path_2, path_1)

def node_C(array, weight, first_node, cleared):
    return node_D(array, weight+array[3], first_node, cleared)

def node_D(array, weight, first_node, cleared):
    return node_A(array, weight+array[0], first_node, cleared)

array = map(int, raw_input().split())

print find_min_path(array)
