import time


def lookup(mapToSearch, open, closed):

    time.sleep(3)

    while(True):
        try:
            x = int(input("Enter x val: "))
            y = int(input("Enter y val: "))
            idxToLookup = (x, y)
            if idxToLookup in closed:
                print(f"f value = {closed[idxToLookup].sumOfHeuristicAndDistanceFromStartToCurrent}\ng value = {closed[idxToLookup].distanceFromStartToCurrent}\n"
                      f"h value = {closed[idxToLookup].sumOfHeuristicAndDistanceFromStartToCurrent - closed[idxToLookup].distanceFromStartToCurrent}")
            elif idxToLookup in open:
                print(f"f value = {open[idxToLookup].sumOfHeuristicAndDistanceFromStartToCurrent}\ng value = {open[idxToLookup].distanceFromStartToCurrent}\n"
                      f"h value = {open[idxToLookup].sumOfHeuristicAndDistanceFromStartToCurrent - open[idxToLookup].distanceFromStartToCurrent}")
            else:
                print("Sorry idx to lookup was not explored")


        except:
            print("Input is invalid!")

