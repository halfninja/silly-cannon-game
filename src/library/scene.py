from __future__ import annotations
from typing import *
from pygame import *
from itertools import chain
from src.library import Renderable
if TYPE_CHECKING:
    from src.library import Manager, Camera

if TYPE_CHECKING:
    from pygame import Surface
    from src.library import Entity


def is_live(entity: Entity):
    return not entity.dead


class Scene(Renderable):
    def __init__(self):
        self.gravity = 2
        self.objects: List[Entity] = []
        self.overlays: List[Entity] = []
        self.bg_color = (0, 0, 0)

    def _all_entities(self) -> Iterator[Entity]:
        return chain(self.objects, self.overlays)

    def _all_live_entities(self) -> Iterator[Entity]:
        return filter(is_live, self._all_entities())

    def add(self, entity: Entity):
        self.objects.append(entity)

    def add_overlay(self, entity: Entity):
        self.overlays.append(entity)

    def update(self, dt: float, manager: Manager):
        for e in self._all_live_entities():
            e.update(dt, manager)
        # TODO evict dead entities

    def render(self, canvas: Surface, camera: Camera):
        canvas.fill(self.bg_color)
        for e in self._all_live_entities():
            e.render(canvas, camera)

    def set_bg(self, bg_color):
        self.bg_color = bg_color
