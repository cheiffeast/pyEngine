import ENGINE
import pygame

world, screen, clock = ENGINE.init([500, 500])
playing = True

objects = [ENGINE.Objects.Player([250, 250], [20, 20]), ENGINE.Objects.SolidObject([100, 100], [100, 20]),
           ENGINE.GIF.GIF([100, 100], [60, 60], "Engine/Textures/Loading")]
world.addObjects(objects)

while playing:
    screen.fill([255, 255, 255])

    inputs = ENGINE.Inputs.getInputs()

    if inputs["quit"]: playing = False

    world.update(inputs)

    pygame.display.update()
    clock.tick(60)

pygame.quit()