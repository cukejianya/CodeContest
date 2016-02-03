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
            #print length
            area_list.append({"x": x, "y": y, "len": length})
            area_list = sorted(area_list, key=lambda k: k["len"], reverse=True)
    for elm in area_list:
         print elm
    return max_product(area_list)

def check_coord_arms(l_elm, l_nxt, elm_y, nxt_y):
    coord_map = {elm_y: l_elm, nxt_y: l_nxt}
    print coord_map
    low_coord = min(elm_y, nxt_y)
    high_coord = max(elm_y, nxt_y)
    if low_coord + coord_map[low_coord] < high_coord - coord_map[high_coord]:
        #If pluses dont overlap, return true to break.
        return True
    else:
        return False


def check_coord_lines(elm_pt, low_pt, high_pt):
    pass

def crossover_check(elm, nxt):
    #if x coords are the same, check for y overlapping
    if elm["x"] is nxt["x"]:
        print "x is ", elm["x"], "and y:"
        return check_coord_arms(elm["len"], nxt["len"], elm["y"], nxt["y"])
    #if y coords are the same, check for x overlapping
    if elm["y"] is nxt["y"]:
        print "y is ", elm["y"], "and x:"
        return check_coord_arms(elm["len"], nxt["len"], elm["x"], nxt["x"])
    return True



def max_product(area_list):
    if (len(area_list) < 2):
        return 0
    products = [0, 1]
    for idx, elm in enumerate(area_list):
        for nxt in area_list[idx+1:]:
            new_elm, new_nxt = elm.copy(), nxt.copy()
            for e_l in range(elm["len"]+1)[::-1]:
                new_elm["len"] = e_l
                for n_l in range(nxt["len"]+1)[::-1]:
                    new_nxt["len"] = n_l
                    prod_of_area = area(new_elm["len"]) * area(new_nxt["len"])
                    if prod_of_area is 81:
                        print prod_of_area,
                    if prod_of_area not in products and crossover_check(new_elm, new_nxt):
                        products.append(prod_of_area)
    print products
    return max(products)



n_m = map(int, raw_input().split())
grid = []
for x in range(n_m[0]):
    grid.append(raw_input())

print tranverse_grid(n_m, grid)
