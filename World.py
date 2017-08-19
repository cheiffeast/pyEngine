import pygame, pickle

class World:
    def __init__(self, screen, **kwargs):
        '''
        The world for the game that will contain all objects for the game
        
        :param kwargs: Keyword arguments
        '''

        self.screen = screen
        self.background = kwargs.get("background", "Textures/missing.jpg")
        self.objects = kwargs.get("objects", [])

    def getObjectById(self, id: str) -> object:
        '''
        Returns the first object with the id given by the user
        
        :param id: The id of the object trying to be found
        :return: If a object is found it will return the object, else it will return None
        '''
        for object in self.objects:
            if object.id == id:
                return object
        return None

    def getObjectsById(self, id: str) -> list:
        '''
        Returns a list of objects that have the same id
        
        :param id: The id of the object trying to be found
        :return: If a object is found it will return the object, else it will return a empty list 
        '''
        objects = [object for object in self.objects if object.id == id]
        return objects

    def addObject(self, object: object) -> int:
        object.world = self
        object.ObjectAdded()
        self.objects.append(object)
        return len(self.objects) - 1

    def addObjects(self, objects: list) -> list:
        indexes = [len(self.objects) + n for n in range(len(objects))]
        for object in objects:
            object.world = self
            object.ObjectAdded()
            self.objects.append(object)
        return indexes

    def update(self, inputs: dict):
        '''
        Update the world, should be called every game loop
        
        :param inputs: Dictionary containing events from pygame
        :return: 
        '''
        for object in self.objects:
            object.update(inputs)

