import pygame


def getInputs() -> dict:
    '''
    Should be called every game loop, handles pygame events and other inputs from the user
    
    :return: Dictionary containing the inputs
    '''

    events = [event for event in pygame.event.get()]
    keys = [key for key in pygame.key.get_pressed()]
    quit = [True for event in events if event.type == pygame.QUIT]
    keysDown = [event for event in events if event.type == pygame.KEYDOWN]
    keysUp = [event for event in events if event.type == pygame.KEYUP]

    return {"events": events, "keys": keys, "quit": quit, "keysDown": keysDown, "keysUp": keysUp}

