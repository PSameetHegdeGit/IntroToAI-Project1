
def readFile(filename):
    f = open("./Maps/"+filename, "r")
    sstart = tuple(map(int, str.split(f.readline())))
    sgoal = tuple(map(int, str.split(f.readline())))
    hardTraverse = []
    for x in range(8):
        hardTraverse.append(tuple(map(int, str.split(f.readline()))))
    completeGrid = []
    for x in range(120):
        row = list(f.readline())
        row = row[:-1]
        completeGrid.append(row)
    f.close()


    for i in range(len(completeGrid)):
        for j in range(len(completeGrid[0])):
            term = completeGrid[i][j]
            if term == '0' or term == '1' or term == '2':
                completeGrid[i][j] = int(term)



    # print(sstart.__str__() + " " + sgoal.__str__() + " " + hardTraverse.__str__() + " " + completeGrid.__str__())
    return sstart, sgoal, hardTraverse, completeGrid






