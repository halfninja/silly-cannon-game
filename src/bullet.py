import pygame
import math

from library import Manager
from locals import *
from settings import *
from library.camera import Camera
from library.entity import Entity
from library.transforms import *
from library.imageloader import get_image


class Bullet(Entity):
    size = 4

    def __init__(self, pos, angle, speed):
        super().__init__()
        self.pos = x, y = pos
        self.rect = Rect(x, y, Bullet.size, Bullet.size)
        self.velocity = Vector2(speed, 0).rotate(-angle)

    def update(self, dt: float, manager: Manager):
        self.pos += self.velocity * dt
        self.velocity.y += manager.scene.gravity
        self.rect.center = self.pos
        if self.pos.y > 0:
            self.dead = True

    def render(self, canvas: Surface, camera: Camera):
        translated_rect = camera.get_rect(self.rect)
        canvas.fill(sprite_color, translated_rect)
