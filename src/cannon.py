import pygame
import math

from bullet import Bullet
from library import Manager
from locals import *
from settings import *
from library.camera import Camera
from library.entity import Entity
from library.transforms import *
from library.imageloader import get_image


class Cannon(Entity):
    def __init__(self):
        super().__init__()
        self.rect = Rect(0, 0, 25, 10)
        self.angle = 45
        self.barrel = Surface((20, 4), pygame.SRCALPHA)
        self.barrel.fill(sprite_color)
        self.shadow = get_image("data/ground_shadow_large.png")
        self.shadow_rect: Rect = self.shadow.get_rect()
        self.shadow_rect.midtop = self.rect.midbottom

    def fire(self, manager: Manager):
        bullet_pos = Vector2(self.rect.midtop) + Vector2(20, 0).rotate(-self.angle)
        bullet = Bullet(bullet_pos, self.angle, 100)
        manager.scene.add(bullet)

    def angle_radians(self) -> float:
        return math.radians(self.angle)

    def update(self, dt: float, manager: Manager):
        self.angle += dt * 20

    def render(self, canvas: Surface, camera: Camera):
        translated_rect = camera.get_rect(self.rect)
        canvas.fill(sprite_color, translated_rect)
        blit_rotate(canvas, self.barrel, translated_rect.center, (2, 2), self.angle)

        canvas.blit(self.shadow, camera.get_rect(self.shadow_rect))

