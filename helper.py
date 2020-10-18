

class CollisionError(Exception):
    pass



def Up(map, row, column, indicesOfPath):

    for x in range(row - 1, row - 21, -1):

        row = x

        if x < 0 or x >= 120:
            break

        if map[x][column] == 'a' or map[x][column] == 'b':
            raise CollisionError()

        if map[x][column] == 1:
            map[x][column] = 'a'
        elif map[x][column] == 2:
            map[x][column] = 'b'


        indicesOfPath.append((x, column))

    return row, column


def Left(map, row, column, indicesOfPath):

    for y in range(column - 1, column - 21, -1):

        column = y


        if y < 0 or y >= 160:
            break

        if map[row][y] == 'a' or map[row][y] == 'b':
            raise CollisionError()

        if map[row][y] == 1:
            map[row][y] = 'a'
        elif map[row][y] == 2:
            map[row][y] = 'b'

        indicesOfPath.append((row, y))

    return row, column


def Right(map, row, column, indicesOfPath):
    for y in range(column + 1, column + 21):

        column = y


        if y < 0 or y >= 160:
            break

        if map[row][y] == 'a' or map[row][y] == 'b':
            raise CollisionError()

        if map[row][y] == 1:
            map[row][y] = 'a'
        elif map[row][y] == 2:
            map[row][y] = 'b'



        indicesOfPath.append((row, y))

    return row, column


def Down(map, row, column, indicesOfPath):


    for x in range(row + 1, row + 21):

        row = x

        if x < 0 or x >= 120:
            break

        if map[x][column] == 'a' or map[x][column] == 'b':
            raise CollisionError()

        if map[x][column] == 1:
            map[x][column] = 'a'
        elif map[x][column] == 2:
            map[x][column] = 'b'


        indicesOfPath.append((x, column))

    return row, column


