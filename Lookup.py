import time


def lookup(mapToSearch):

    time.sleep(4)

    while(True):
        try:
            x = int(input("Enter x val: "))
            y = int(input("Enter y val: "))
            print(mapToSearch[x][y])

        except:
            print("Input is invalid!")

