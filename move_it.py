import numpy
import pygame

def move(map, loc, done, times, event):
    x, y = loc[0], loc[1]
    entry = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    cho_list = []
    for cho_f in entry:
        xi, yi = x + cho_f[0], y + cho_f[1]
        if 5 >= xi >= 0 and 5 >= yi >= 0:
            if map[xi][yi] == 0:
                cho_list.append([xi, yi])
    if cho_list == []:
        return map, loc, True, times
    for cho_e in cho_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym = pygame.mouse.get_pos()
            if cho_e[0]*100 <= xm <= cho_e[0]*100 + 100 and cho_e[1]*100 <= ym <= cho_e[1]*100 + 100:
                times += 1
                map[cho_e[0]][cho_e[1]] = times
                loc[0], loc[1] = cho_e[0], cho_e[1]
                return map, loc, done, times
    return map, loc, done, times