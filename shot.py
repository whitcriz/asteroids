import pygame
from circleshape import *
from constants import *
from asteroid import *

class Shot(Asteroid):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    

