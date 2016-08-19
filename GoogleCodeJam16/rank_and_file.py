# import sys
#
# sys.stdout = open("./ans.out", 'w')

def findMissingList(grid, n):
    highArray = map(max, grid)
    lowArray = map(min, grid)
    highest = max(highArray)
    lowest = min(lowArray)
    sortedGrid = sorted(grid, key=lambda arr: arr[0])
    # print sortedGrid, highArray, lowArray, lowest, highest
    row, col = [], []
    if lowArray.count(lowest) == 2:
        row.append(sortedGrid.pop(0))
        col.append(sortedGrid.pop(0))
    for idx in range(1, len(row[0])- 1):
        if (checkFit(row, sortedGrid[0], idx)):
            row.append(sortedGrid.pop(0))
            if (checkFit(col, sortedGrid[0], idx)):
                col.append(sortedGrid.pop(0))
        else:
            col.append(sortedGrid.pop(0))
            if (checkFit(row, sortedGrid[0], idx)):
                row.append(sortedGrid.pop(0))
    print row
    print col

def checkFit(aList, array, idx):
    for i in range(idx):
        if aList[i][idx] is not array[i]:
            return True
    return False




with open('input.in') as inp:
    count, nxt = 0, 1
    for idx, line in enumerate(inp):
        if idx is 0:
            t = int(line)
            continue
        if idx == nxt:
            array = []
            n = int(line)
            nxt = idx + 2*n
            count += 1
        else:
            array.append(map(int, line.split(" ")))
        if idx == nxt - 1:
            print 'Case #%d: %s' %(count, findMissingList(array, n))
