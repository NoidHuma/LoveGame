import random
import pygame
#import secondaryFunc


backgroundsCount = 7


def transformScaleKeepRatio(image, size):
    iwidth, iheight = image.get_size()
    scale = max(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size)
    return scaled_image


def choose_background(screen):
    img_num = random.randint(1, backgroundsCount)
    menu_background = pygame.image.load('images/peach_goma_img' + str(img_num) + '.jpg').convert()
    menu_background = transformScaleKeepRatio(menu_background, (1024, 640))
    screen.blit(menu_background, (0,0))
    pygame.display.update()
    return [menu_background, img_num]


def change_background(screen, img_num):
    if img_num == backgroundsCount:
        img_num = 1
    else:
        img_num += 1
    menu_background = pygame.image.load('images/peach_goma_img' + str(img_num) + '.jpg').convert()
    menu_background = transformScaleKeepRatio(menu_background, (1024, 640))
    #pygame.display.update()
    return [menu_background, img_num]