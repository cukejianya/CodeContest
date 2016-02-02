def area(length):
    return length*4 + 1

def check_left(x, y, n, m, grid, mx):
    length = 0
    for curr_x in range(x)[::-1]:
        if grid[y][curr_x] is "B" or length >= mx:
            break
        length += 1
    return length

def check_up(x, y, n, m, grid, mx):
    length = 0
    for curr_y in range(y)[::-1]:
        if grid[curr_y][x] is "B" or length >= mx:
            break
        length += 1
    return length

def check_right(x, y, n, m, grid, mx):
    length = 0
    x += 1
    for curr_x in range(x, m):
        # "Check Right", curr_x, y
        if grid[y][curr_x] is "B" or length >= mx:
            break
        length += 1
    return length

def check_down(x, y, n, m, grid, mx):
    length = 0
    y += 1
    for curr_y in range(y, n):
        if grid[curr_y][x] is "B" or length >= mx:
            break
        length += 1
    return length


def check_plus(coord, n_m, grid):
    x,y,n,m = coord[0], coord[1], n_m[0], n_m[1]
    switcher = [
        check_left,
        check_up,
        check_right,
        check_down
    ]
    max_length = m
    for corner in range(4):
        length = switcher[corner](x, y, n, m, grid, max_length)
        max_length = min(length, max_length)
        if not max_length:
            break

    return max_length

def tranverse_grid(n_m, grid):
    area_list = []
    plus_dict = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell is "B":
                continue
            length = check_plus([x, y], n_m, grid)
            print length
            area_list.append([" ".join([str(x), str(y)]), length])
            area_list = sorted(area_list, key=lambda k: k[1], reverse=True)
    # for elm in area_list:
    #     print elm
    return max_product(area_list)

def check_x()


def

def crossover_check(elm, nxt):
    l_elm, l_nxt = elm[1], nxt[1]
    coord_elm, coord_nxt = map(int, elm[0].split()), map(int, nxt[0].split())
    if coord_elm[0] is coord_nxt[0]:



def max_product(area_list):
    if (len(area_list) < 2):
        return 0
    products = [0]
    for idx, elm in enumerate(area_list):
        coord_elm = map(int, elm[0])
        for nxt in area_list[idx:]:
            coord = map(int, elm[0])
            if


n_m = map(int, raw_input().split())
grid = []
for x in range(n_m[0]):
    grid.append(raw_input())

tranverse_grid(n_m, grid)
