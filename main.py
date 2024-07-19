import pygame
import sys
import random
import math
from scripts.Constants import *
from scripts.utilis import Generate_lst, Draw
from sorting.Bubble_Sort import bubble_sort
from sorting.Insertion_Sort import insertion_sort
from sorting.Selection_Sort import selection_sort
from sorting.Merge_Sort import merge_sort


# pygame Initialization
pygame.init()

# Graphics Information
class Sorting_GUI_Information:
    def __init__(self, lst):
        self.lst = lst
        self.set_list(lst)
        
        # pygame
        self.screen = pygame.display.set_mode((SIZE["Width"],SIZE["Height"]))
        pygame.display.set_caption("Sorting Algorithms Visualizer")
        
        

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        """Total area we get to draw / length of the list"""
        self.bar_width = round((SIZE["Width"] - PADDING["side"]) / len(lst))
        """Total area be grt to draw / number of values in my range
            here 'my range'= (max_val - min_val)
        """
        self.bar_height = math.floor((SIZE["Height"] - PADDING["top"]) / (self.max_val - self.min_val))
        
        # an x co-ordinate to start drawing
        self.start_x = PADDING['side'] // 2



def Main():
    clock = pygame.time.Clock()

    # variables
    running = True
    sorting = False
    ascending = False
    descending = False

    #sorting Variables
    sorting_algorithm = merge_sort
    sorting_name = 'Merge Sort'
    sorting_algorithm_generator = None

    #lst variables
    n = 100
    min_val = 0
    max_val = 100
    # draw
    starting_lst = Generate_lst(n, min_val, max_val)
    draw_info = Sorting_GUI_Information(starting_lst)

    
    #event loop
    while running:
        dt = clock.tick(60) / 1000

        # Algorithm generator 
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            Draw(draw_info, sorting_name, ascending)

        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            # mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mos_x , mos_y = event.pos
                if SIZE["Width"] - 100 <= mos_x <= SIZE["Width"] - 25 and 0 <= mos_y <= 20:
                    starting_lst = Generate_lst(n, min_val, max_val)
                    draw_info.set_list(starting_lst)
                    sorting = False
                if SIZE["Width"] - 75 <= mos_x <= SIZE["Width"] - 25 and 50 <= mos_y <= 80:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

                      

            # keyboard events
            if event.type  != pygame.KEYDOWN:
                continue
            
            elif event.key == pygame.K_r:
                starting_lst = Generate_lst(n, min_val, max_val)
                draw_info.set_list(starting_lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_UP and not sorting:
                ascending = True
                descending = False
            elif event.key == pygame.K_DOWN and not sorting:
                descending = True
                ascending = False
        #update display
        pygame.display.update()


if __name__ == "__main__":
    Main()