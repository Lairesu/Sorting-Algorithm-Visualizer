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

def Draw(draw_info):
    draw_info.screen.fill(COLOR["bg_color"])
    Draw_list(draw_info)
    draw_button(draw_info)
    draw_text(draw_info)
    pygame.display.update()


def Draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = (draw_info.start_x + i * draw_info.bar_width)
        y = SIZE["Height"] - (val - draw_info.min_val) * draw_info.bar_height

        color = COLOR["yellow"]
        pygame.draw.rect(draw_info.screen, color ,(x,y, draw_info.bar_width,(val-draw_info.min_val) * draw_info.bar_height),)


def draw_button(draw_info):
    font = pygame.font.Font(None, 30)
    font_surf = font.render("Generate", 1,COLOR["text"],)
    font_rect = font_surf.get_rect(center=(SIZE["Width"] - 50, 20))
    pygame.draw.rect(draw_info.screen, COLOR["cyan"], font_rect)
    draw_info.screen.blit(font_surf, font_rect)


def draw_text(draw_info):
    Header = pygame.font.Font(None, 40)
    Header_surf = Header.render("SORTING ALGORITHM", 1, COLOR["green"],)
    draw_info.screen.blit(Header_surf, ((SIZE["Width"] / 2) - (Header_surf.get_width()/2), 5))
