import sys
class FileReader:
    def __init__(self):
        f = open("demofile.txt", "r")
        sstart = str.split(f.readline())
        sgoal = str.split(f.readline())
        hardTraverse = []
        for x in range(8):
            hardTraverse.append(str.split(f.readline()))
        completeGrid = []
        for x in range(120):
            completeGrid.append(list(f.readline()))
        f.close()