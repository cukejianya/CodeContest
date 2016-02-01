def check_left(x, y, n, m, grid, mx):
    for curr_x in range(0, x)[::-1]:
        if grid[curr_x][y] is "B":
            break
        length += 1
    return length

def check_up(x, y, n, m, grid, mx):
    print "works"

def check_right(x, y, n, m, mx):
    print "yeah"
def check_down(x, y, n, m, mx):
    print "love"


def check_plus(coord, n_m, grid):
    x,y,n,m = coord[0], coord[1], n_m[0], n_m[1]
    switcher = [
        check_left,
        check_up,
        check_right,
        check_down
    ]
    max_length = 0;
    for corner in range(4):
        length = switcher[corner](x, y, n, m, grid, max_length)
        max_length = min(length, max_length)



n_m = raw_input.split()
grid = []
for x in range(n_m[0])
    grid.append(x)
