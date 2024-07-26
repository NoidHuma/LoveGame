import random
import pygame


def start_music():
    pygame.mixer.music.load('sounds/background music/Soothing Relaxation - Relaxing Romantic Music ★101.mp3')
    pygame.mixer.music.play(-1, random.randint(1, 33) * 60)
    pygame.mixer.music.set_volume(0)


def volume_increase(nowVolume):
    if nowVolume < 1:
        nowVolume += 0.005
        pygame.mixer.music.set_volume(nowVolume)
    return nowVolume