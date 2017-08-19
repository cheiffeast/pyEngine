from . import World, Objects, Inputs, GIF
import pygame

def init(size):
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    world = World.World(screen)

    return world, screen, clock