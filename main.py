import pygame
import random
import backgroundLogic


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

backgroundLogic.choose_background(screen)

# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

