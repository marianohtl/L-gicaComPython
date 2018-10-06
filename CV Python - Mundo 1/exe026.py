'''import pygame
pygame.mixer.init() #*
pygame.mixer.music.load('exe026.mp3') #exe026.mp3 - PASTE
pygame.mixer.music.play()
input() #*

#*comandos não correspondem a aula original'''

import pygame
pygame.mixer.init() # acréscimo ao código original
pygame.init()
pygame.mixer.music.load('exe026.mp3')
pygame.mixer.music.play()
pygame.event.wait()
