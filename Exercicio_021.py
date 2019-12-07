import pygame

# Rodar Música no python

pygame.mixer.init()
pygame.mixer.music.load('d:/musicas/leonardo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


