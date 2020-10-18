from FormingMap import *
from FileWriter import *


def ReadyMapForWrite(mapToSearch):
    for i in range(len(mapToSearch)):
        for j in range(len(mapToSearch[i])):
            mapToSearch[i][j] = str(mapToSearch[i][j])


def GenerateMaps(noOfMaps, noOfStartAndEndIdx):

    for i in range(noOfMaps):
        instanceOfMap = MapData()
        instanceOfMap.runSuite()
        ReadyMapForWrite(instanceOfMap.map)
        for j in range(noOfStartAndEndIdx):
            start, end = instanceOfMap.generateStartAndEndIndices()
            FileWriter(start, end, instanceOfMap.hardToTraverseIndices, instanceOfMap.map, f"Maps/map_{i}_{j}.txt")


if __name__ == "__main__":
    GenerateMaps(5, 10)




