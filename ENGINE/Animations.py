import pygame, os


class GIF:
    def __init__(self, position: list, size: list, folder: str, **kwargs):
        self.position = position
        self.size = size
        self.surface = pygame.Surface(size)
        self.folder = folder
        self.frames = [pygame.transform.scale(pygame.image.load(folder + "/" +file), size) for file in os.listdir(folder)]

        self.playbackSpeed = kwargs.get("speed", 2)
        self.index = 0
        self.count = 0
        self.solid = 0

    def ObjectAdded(self):
        '''
        Called when the object is added to the world 
        '''
        pass

    def onRefresh(self, inputs: dict):
        '''
        Called every refresh loop and is used for anything other than drawing that may want to be done

        :param inputs: A dictionary containing events from inputs
        '''

        pass

    def draw(self, inputs: dict):
        self.surface.fill([255, 255, 255])
        self.count += 1
        if self.count % self.playbackSpeed == 0:
            self.count = 0
            self.index += 1
            if self.index == len(self.frames): self.index = 0

        self.surface.blit(self.frames[self.index], [0, 0])
        return self.surface, self.position

    def update(self, inputs: dict):
        surface, position = self.draw(inputs)
        self.world.screen.blit(surface, position)