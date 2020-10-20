class FileReader:
    def __init__(self):
        self.readFile()
    @staticmethod
    def readFile(filename):
        f = open("./Maps/"+filename, "r")
        sstart = list(map(int, str.split(f.readline())))
        sgoal = list(map(int, str.split(f.readline())))
        hardTraverse = []
        for x in range(8):
            hardTraverse.append(list(map(int, str.split(f.readline()))))
        completeGrid = []
        for x in range(120):
            row = list(f.readline())
            row = row[:-1]
            completeGrid.append(row)
        f.close()
        print(sstart.__str__() + " " + sgoal.__str__() + " " + hardTraverse.__str__() + " " + completeGrid.__str__())
        return sstart, sgoal, hardTraverse, completeGrid

if __name__ == "__main__":
    FileReader()

