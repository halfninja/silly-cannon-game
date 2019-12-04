from locals import *
from library.camera import Camera

class Entity:
    def __init__(self, rect: Rect):
        self.rect = rect

    def update(self, dt: float): pass

    def render(self, canvas: Surface, camera: Camera): pass
