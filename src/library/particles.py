import random

from dataclasses import dataclass
from typing import Optional

from pygame import Surface, Vector2, Rect

from library import Entity, Manager, Camera


@dataclass
class P:
    __slots__ = ['x', 'y', 'vx', 'vy', 'life']
    x: float
    y: float
    vx: float
    vy: float
    life: Optional[float]


class Particles(Entity):
    def __init__(self):
        super().__init__()
        self._p = []
        self.color = (0, 0, 0)
        self.width = 1
        self.gravity_enabled = True

    def update(self, dt: float, manager: Manager):
        g = None
        if self.gravity_enabled:
            g = manager.scene.gravity
        for p in self._p:
            if p.x is not None:
                p.life -= dt
                if p.life > 0.0:
                    p.x += p.vx * dt
                    p.y += p.vy * dt
                    if g is not None:
                        p.vy += g * dt
                    if p.y > 0 and p.vy > 0:
                        if p.vy > 20.0:
                            p.vy *= -0.8
                            p.vx *= 0.8
                        else:
                            # time to die
                            p.x = None
                else:
                    p.x = None
        # TODO clear up or reuse dead particles

    def add(self, x: float, y: float, vx: float, vy: float, life: float = 60.0):
        self._p.append(P(x, y, vx, vy, life))

    def semicircle_explosion(self, x: float, y: float, strength: float, count: int):
        for _ in range(count):
            v = Vector2(random.uniform(strength * 0.5, strength), 0).rotate(-random.uniform(0, 180))
            life = random.uniform(1.0, 2.0)
            self.add(x, y, v.x, v.y, life)

    def render(self, canvas: Surface, camera: Camera):
        for p in self._p:
            if p.x is not None:
                translated_rect = camera.get_rect(Rect(p.x, p.y, 1, 1))
                canvas.fill(self.color, translated_rect)