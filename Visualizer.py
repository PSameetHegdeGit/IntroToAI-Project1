import pygame, sys
import xlsxwriter
import AlgorithmImplementation
from AlgorithmImplementation import *
from FileReader import readFile
from FormingMap import *
import threading
import timeit
import psutil
from Lookup import lookup

def get_tile_color(tile_contents):

    tile_color = None
    if tile_contents == 0:
        tile_color = constants.BLACK
    elif tile_contents == 1:
        tile_color = constants.GREY
    elif tile_contents == 2:
        tile_color = constants.DARKORANGE
    elif tile_contents == 'a':
        tile_color = constants.BLUE
    elif tile_contents == 'b':
        tile_color = constants.UGLY_PINK

    # For the optimal path
    elif tile_contents == 'optimal':
        tile_color = constants.GREEN


    return tile_color

def draw_map(surface, map_rows):
    for j, row in enumerate(map_rows):
        for i, tile in enumerate(row):
            myrect = pygame.Rect(i*constants.BLOCK_WIDTH, j*constants.BLOCK_HEIGHT, constants.BLOCK_WIDTH, constants.BLOCK_HEIGHT)
            pygame.draw.rect(surface, get_tile_color(tile), myrect)

def draw_grid(surface):
    for i in range(constants.NUMBER_OF_BLOCKS_WIDE):
        new_height = round(i * constants.BLOCK_HEIGHT)
        new_width = round(i * constants.BLOCK_WIDTH)
        pygame.draw.line(surface, constants.BLACK, (0, new_height), (constants.SCREEN_WIDTH, new_height), 2)
        pygame.draw.line(surface, constants.BLACK, (new_width, 0), (new_width, constants.SCREEN_HEIGHT), 2)

def game_loop(surface, world_map):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        draw_map(surface, world_map)
        draw_grid(surface)
        pygame.display.update()

def initialize_game():
    pygame.init()
    surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption(constants.TITLE)
    surface.fill(constants.BLACK)
    return surface


# We can use this for reading a file -- For now we can just generate an arbitrary map
def read_map(mapfile):
    with open(mapfile, 'r') as f:
        world_map = f.readlines()
    world_map = [line.strip() for line in world_map]
    return (world_map)


# on Main thread, the pygame visualizaiton will run; on worker thread, a tkinter box will output val for index searched

def chooseAlgorithm(instanceOfMap, startidx, endidx):

    algorithmChoice = input("What Algorithm you would like to Implement?\n").lower()
    open, closed = None, None

    if algorithmChoice == "uniformcostsearch":
        open, closed = UniformCost(startidx, endidx, instanceOfMap.map)
    elif algorithmChoice == "unweightedastarsearch":
        open, closed = UnweightedAstarSearch(startidx, endidx, instanceOfMap.map)
    elif algorithmChoice == "weightedastarsearch":
        weight = float(input("What weight would you like to test with?\n"))
        open, closed = WeightedAstarSearch(startidx, endidx, instanceOfMap.map, weight)
    elif algorithmChoice == "multipleastarsearch":
        pass
        # open, closed = WeightedAstarSearch(instanceOfMap.startindex, instanceOfMap.endIndex, instanceOfMap.map, 2.5)

    threadmanaginglookup = threading.Thread(target=lookup, args=(instanceOfMap.map, open, closed,), daemon=True)

    threadmanaginglookup.start()

def testSuite():
    # wb = xlsxwriter.Workbook('list.xlsx')
    # sheet = wb.add_worksheet()
    # headers = ["MAP #", "UC RUNTIME", "UC MEM USAGE", "UC PATH LENGTH/OPTIMAL LENGTH", "UC NUM NODES EXPANDED",
    #             "A* RUNTIME", "A* MEM USAGE", "A* PATH LENGTH/OPTIMAL LENGTH", "A* NUM NODES EXPANDED",
    #             "1.25 WEIGHT A* RUNTIME", "1.25 WEIGHT A* MEM USAGE", "1.25 WEIGHT A* PATH LENGTH/OPTIMAL LENGTH", "1.25 WEIGHT A* NUM NODES EXPANDED",
    #             "2 WEIGHT A* RUNTIME", "2 WEIGHT A* MEM USAGE", "2 WEIGHT A* PATH LENGTH/OPTIMAL LENGTH", "2 WEIGHT A* NUM NODES EXPANDED"]
    # for col_num, data in enumerate(headers):
    #     sheet.write(0, col_num, data)
    for x in range(50):
        print(x)
        filename = "map_" + str(x // 10) + "_" + str(x % 10) + ".txt"
        startidx, endidx, hardTraverse, completeGrid = readFile(filename)
        startidx2, endidx2, hardTraverse2, completeGridUnweighted = readFile(filename)
        startidx3, endidx3, hardTraverse3, completeGridSmallWeighted = readFile(filename)
        startidx4, endidx4, hardTraverse4, completeGridLargeWeighted = readFile(filename)
        # starttime = timeit.default_timer()




        openUniformCost, closedUniformCost = UniformCost(startidx, endidx, completeGrid)
        # ucmem = psutil.virtual_memory().percentage
        # ucruntime = timeit.default_timer() - starttime
        # ucnodes = len(closedUniformCost) + len(openUniformCost)
        # ucpath = AlgorithmImplementation.backtrackTesting(closedUniformCost[endidx], startidx, completeGrid)
        # starttime = timeit.default_timer()
        openUnweightedStar, closedUnweightedStar = UnweightedAstarSearch(startidx2, endidx2, completeGridUnweighted)
        # amem = psutil.virtual_memory().percentage
        # aruntime = timeit.default_timer() - starttime
        # anodes = len(closedUnweightedStar) + len(openUnweightedStar)
        # apath = AlgorithmImplementation.backtrackTesting(closedUnweightedStar[endidx], startidx, completeGrid)
        # starttime = timeit.default_timer()
        openSmallWeightedStar, closedSmallWeightedStar = WeightedAstarSearch(startidx3, endidx3, completeGridSmallWeighted, 1.5)
        # swmem = psutil.virtual_memory().percentage
        # swruntime = timeit.default_timer() - starttime
        # swnodes = len(closedSmallWeightedStar) + len(openSmallWeightedStar)
        # swpath = AlgorithmImplementation.backtrackTesting(closedSmallWeightedStar[endidx], startidx, completeGrid)
        # starttime = timeit.default_timer()
        openLargeWeightedStar, closedLargeWeightedStar = WeightedAstarSearch(startidx4, endidx4, completeGridLargeWeighted, 5)
        # lwmem = psutil.virtual_memory().percentage
        # lwruntime = timeit.default_timer() - starttime
        # lwnodes = len(closedLargeWeightedStar) + len(openLargeWeightedStar)
        # lwpath = AlgorithmImplementation.backtrackTesting(closedLargeWeightedStar[endidx], startidx, completeGrid)
        # row = [x, ucruntime, ucmem, ucpath, ucnodes, aruntime, amem, apath, anodes, swruntime, swmem, swpath, swnodes, lwruntime, lwmem, lwpath, lwnodes]
        # for col_num, data in enumerate(row):
        #     sheet.write(x+1, col_num, data)
        # wb.close()

def main():

    # Choosing algorithm
    instanceOfMap = MapData()
    instanceOfMap.runSuite()
    startidx, endidx = instanceOfMap.generateStartAndEndIndices()

    chooseAlgorithm(instanceOfMap, startidx, endidx)


    surface = initialize_game()


    game_loop(surface, instanceOfMap.map)
    # testSuite()

if __name__=="__main__":
    main()

