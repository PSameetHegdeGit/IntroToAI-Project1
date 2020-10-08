import pygame, sys
import constants
from FormingMap import *

def get_tile_color(tile_contents):

    tile_color = None
    if tile_contents == 0:
        tile_color = constants.BLACK
    elif tile_contents == 1:
        tile_color = constants.GREY
    elif tile_contents == 2:
        tile_color = constants.DARKORANGE
    elif tile_contents == 3:
        tile_color = constants.GREEN
    elif tile_contents == 4:
        tile_color = constants.UGLY_PINK

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

def main():
    # world_map = read_map(constants.MAPFILE)
    instanceOfMap = MapData()
    instanceOfMap.runSuite()



    surface = initialize_game()

    game_loop(surface, instanceOfMap.map)

if __name__=="__main__":
    main()

