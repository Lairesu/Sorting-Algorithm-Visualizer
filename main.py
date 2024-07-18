import pygame
import sys
import random
from scripts.Constants import *
from scripts.utilis import Generate_lst, Draw

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
        self.bar_height = round((SIZE["Height"] - PADDING["top"]) / (self.max_val - self.min_val))
        
        # an x co-ordinate to start drawing
        self.start_x = PADDING['side'] // 2



def Main():
    clock = pygame.time.Clock()
    running = True
    sorting = False

    #lst variables
    n = 20
    min_val = 5
    max_val = 100
    # draw
    starting_lst = Generate_lst(n, min_val, max_val)
    draw_info = Sorting_GUI_Information(starting_lst)

    
    #event loop
    while running:
        dt = clock.tick(60) / 1000
        Draw(draw_info)
        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            # mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mos_x , mos_y = event.pos
                if SIZE["Width"] - 100 <= mos_x <= SIZE["Width"] - 25 and 10 <= mos_y <= 30:
                    starting_lst = Generate_lst(n, min_val, max_val)
                    draw_info.set_list(starting_lst)
                    sorting = False

            # keyboard events
            if event.type  != pygame.KEYDOWN:
                continue
            
            elif event.key == pygame.K_r:
                    starting_lst = Generate_lst(n, min_val, max_val)
                    draw_info.set_list(starting_lst)
                    sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                    sorting = True



        #update display
        pygame.display.update()


if __name__ == "__main__":
    Main()