"""
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame

pygame.mixer.init()

pygame.mixer.music.load(r'C:\Users\Victor\PycharmProjects\CursoemVideo\pythonProject\negrodrama.mp3')

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
