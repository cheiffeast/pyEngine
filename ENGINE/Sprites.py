import pygame, os

class GenericSprite:
    def __init__(self, position: list, size: list, **kwargs):
        '''
        The Genericsprite class will be inherited by almost all sprite

        :param position: position of the sprite in pixels
        :param size: size of the sprite in pixels
        :param kwargs: Keyword arguments
        '''

        self.position = position
        self.x, self.y = self.position
        self.size = size
        self.width, self.height = self.size
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.surface = pygame.Surface(self.size)
        self.lastRefresh = 0

        self.id = kwargs.get("id", None)
        self.surface.set_alpha(kwargs.get("alpha", 255))
        self.texture = pygame.transform.scale(pygame.image.load(kwargs.get("texture", os.path.join(os.getcwd(), "Textures/missing.jpg")), self.size))
        self.refreshRate = kwargs.get("refreshRate", 1)
        self.solid = kwargs.get("solid", 0)

    def updatePosition(self, position: str):
        '''
        Updates the position of the Sprite

        :param position: the new position of the sprite
        '''

        self.position = position
        self.x, self.y = position
        self.rect = pygame.Rect(position[0], position[1], self.size[0], self.size[1])

    def changeTexture(self, image: str):
        '''
        Change the texture of the sprite

        :param image: String of the path to the texture
        '''

        self.texture = pygame.transform.scale(pygame.image.load(image), self.size)

    def changeState(self, solid):
        self.solid = solid

    def spriteAdded(self):
        '''
        Called when the sprite is added to the world 
        '''
        pass

    def onRefresh(self, inputs: dict):
        '''
        Called every refresh loop and is used for anything other than drawing that may want to be done

        :param inputs: A dictionary containing events from inputs
        '''

        pass

    def draw(self, inputs: dict):
        '''
        Called every refresh loop and is used to draw to the screen

        :param inputs: A dictionary containing events from inputs
        '''

        self.surface.fill([255, 255, 255])
        self.surface.blit(self.texture, [0, 0])
        return self.surface, self.position

    def update(self, inputs: dict) -> bool:
        '''
        Called on every game loop

        :param inputs: A dictionary containing events from inputs
        :return: True if the sprite was refreshed and false if it was not
        '''

        self.lastRefresh += 1

        if self.lastRefresh % self.refreshRate == 0:
            self.lastRefresh = 0
            self.onRefresh(inputs)
            surface, position = self.draw(inputs)
            self.world.screen.blit(surface, position)
            return True
        return False

class Player(GenericSprite):
    def __init__(self, position: list, size: list, **kwargs):
        '''
        Player object
    
        :param position: The position of the top-left of the player
        :param size: The width and height of the player
        :param kwargs: Keyword arguments
        '''
        GenericSprite.__init__(self, position, size, **kwargs)

        self.speed = kwargs.get("speed", 2)
        self.offset = [0, 0]
        self.id = kwargs.get("id", "player")
        self.solid = 1


    def onRefresh(self, inputs: dict):
        '''
        Called on refresh
    
        :param inputs: A dictionary containing pygame events and inputs
        :return: 
        '''
        dy, dx = 0, 0
        if inputs["keys"][pygame.K_w]: dy = -self.speed
        if inputs["keys"][pygame.K_s]: dy = self.speed
        if inputs["keys"][pygame.K_a]: dx = -self.speed
        if inputs["keys"][pygame.K_d]: dx = self.speed

        self.singleAxis(dx, 0)
        self.singleAxis(0, dy)
        self.offset = [self.x - 250, self.y - 250]


    def singleAxis(self, dx: int, dy: int):
        '''
        Update a single axis of the player
    
        :param dx: Change in x
        :param dy: Change in y
        '''

        self.updatePosition([self.x + dx, self.y + dy])
        rects = [object.rect for object in self.world.objects if object != self and object.solid]
        collisions = self.rect.collidelistall(rects)
        for collision in collisions:
            if dx > 0:
                self.updatePosition([rects[collision].left - self.rect.width, self.y])
            if dx < 0:
                self.updatePosition([rects[collision].right, self.y])
            if dy > 0:
                self.updatePosition([self.x, rects[collision].top - self.rect.height])
            if dy < 0:
                self.updatePosition([self.x, rects[collision].bottom])

    def draw(self, inputs: dict):
        self.surface.fill([0, 0, 0])
        self.surface.blit(self.texture, [0, 0])
        return self.surface, [250, 250]