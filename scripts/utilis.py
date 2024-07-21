import pygame
import random
from scripts.Constants import *

def Generate_lst(n,min_val,max_val):
    """
    Generates a list of n random integers between min_val and max_val (inclusive).
    """
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def Draw(draw_info, sort_name, ascending):
    draw_info.screen.fill(COLOR["bg_color"])
    Draw_list(draw_info)
    draw_button(draw_info)
    draw_text(draw_info, sort_name, ascending)
    pygame.display.update()


def Draw_list(draw_info, color_pos={}, clear_bg=False):
    lst = draw_info.lst

    # clear certain part of background when sorting
    if clear_bg:
        clear_rect =  (PADDING["side"] // 2 , PADDING["top"],
                       SIZE["Width"] - PADDING["side"],
                       SIZE["Height"] - PADDING["top"])
        pygame.draw.rect(draw_info.screen, COLOR["bg_color"], clear_rect,)


    for i, val in enumerate(lst):
        x = (draw_info.start_x + i * draw_info.bar_width)
        y = SIZE["Height"] - (val - draw_info.min_val) * draw_info.bar_height

        color = COLOR["yellow"]

        # give color to swap and checking color
        if i in color_pos:
            color = color_pos[i]

        pygame.draw.rect(draw_info.screen, color ,(x,y, draw_info.bar_width,(val-draw_info.min_val) * draw_info.bar_height),)

    if clear_bg:
        pygame.display.update()


def draw_button(draw_info):
    font = pygame.font.Font(None, 30)

    # Generate
    font_surf = font.render("Generate", 1,COLOR["text"])
    font_rect = font_surf.get_rect(center=(SIZE["Width"] - 50, 10))
    pygame.draw.rect(draw_info.screen, COLOR["white"], font_rect)
    draw_info.screen.blit(font_surf, font_rect)

    # Sort
    sort_surf = font.render("Sort", 1,COLOR["text"])
    sort_rect = sort_surf.get_rect(center=(SIZE["Width"] -50, 60))
    pygame.draw.rect(draw_info.screen, COLOR["white"], sort_rect)
    draw_info.screen.blit(sort_surf, sort_rect)

def draw_text(draw_info, sort_name, ascending):
    Type = pygame.font.Font(None, 40)
    #type of sorting and descending and Ascending
    Title = Type.render(f"{sort_name} - {'Ascending' if ascending else 'Descending'}", 1, COLOR['text'])
    draw_info.screen.blit(Title, ((SIZE["Width"] / 2) - (Title.get_width()/2), 5))



