import pygame
import backgroundLogic
import random
# import secondaryFunc


# инициализируем библиотеку Pygame
import musicLogic

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

# выбор фонового изображения
background = backgroundLogic.choose_background(screen)

#
clock = pygame.time.Clock()


# переменные для смены фона
backgroundTransp = 255.0
backgroundTranspAcceler = 0.0
changeNow = False

# фоновая музыка
musicLogic.start_music()
nowVolume = 0.0

run = True
while run:
    # устанавливаем 30 фреймов
    clock.tick(30)

    #начало проигрывания музыки
    nowVolume = musicLogic.volume_increase(nowVolume)

    for event in pygame.event.get():
        # обработка закрытия приложения
        if event.type == pygame.QUIT:
            run = False

    # смена фона
    if pygame.time.get_ticks() % 10000 < 100:
        background = backgroundLogic.change_background(screen, background[1])
        changeNow = True
        backgroundTransp = 0
        backgroundTranspAcceler = 0.0

    # обеспечение плавности смены
    if changeNow:
        if backgroundTransp >= 250:
            backgroundTransp = 255
            changeNow = False
        else:
            backgroundTransp += 0.1 + backgroundTranspAcceler
            backgroundTranspAcceler += 0.02
        background[0].set_alpha(backgroundTransp)


    # отрисовка фона
    screen.blit(background[0], (0, 0))

    # обновление окна
    pygame.display.update()


pygame.quit()
exit()

