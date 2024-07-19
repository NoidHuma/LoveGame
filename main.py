import pygame
import backgroundLogic
#import secondaryFunc


# инициализируем библиотеку Pygame
pygame.init()

# определяем размеры окна
window_size = (1024, 640)

# задаем название окна
pygame.display.set_caption("Love Game")

# создаем окно
screen = pygame.display.set_mode(window_size)

# задаем цвет фона
background_color = (225,132,160)

# заполняем фон заданным цветом
screen.fill(background_color)

# обновляем экран для отображения изменений
pygame.display.flip()

background = backgroundLogic.choose_background(screen)
backgroundTransp = 255
changeNow = False

runningTime = 0

run = True
while run:
    pygame.time.delay(50)
    runningTime += 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if runningTime % 30000 == 0:
        background = backgroundLogic.change_background(screen, background[1])
        changeNow = True
        backgroundTransp = 0

    if changeNow:
        if backgroundTransp >= 254:
            backgroundTransp = 255
            changeNow = False
        else:
            backgroundTransp += 1
        background[0].set_alpha(backgroundTransp)

    screen.blit(background[0], (0, 0))

    pygame.display.update()


pygame.quit()
exit()

