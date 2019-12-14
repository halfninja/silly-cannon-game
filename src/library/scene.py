from __future__ import annotations
from typing import *
from pygame import *
from itertools import chain
from library import Renderable
if TYPE_CHECKING:
    from library import Manager, Camera

if TYPE_CHECKING:
    from pygame import Surface
    from library import Entity


def is_live(entity: Entity):
    return not entity.dead


class Scene(Renderable):
    def __init__(self):
        self.gravity: float = 200.0
        self.objects: List[Entity] = []
        self.overlays: List[Entity] = []
        self.names: Dict[str, Entity] = {}
        self.bg_color = (0, 0, 0)

    def _all_entities(self) -> Iterator[Entity]:
        return chain(self.objects, self.overlays)

    def _all_lists(self) -> list[list[Entity]]:
        return [self.objects, self.overlays]

    def _all_live_entities(self) -> Iterator[Entity]:
        return filter(is_live, self._all_entities())

    def find_by_name(self, name: str) -> Entity:
        try:
            return self.names[name]
        except KeyError as e:
            raise KeyError(e, "No entity with name %s" % name)

    def add(self, entity: Entity):
        self.objects.append(entity)
        if entity.name is not None:
            self.names[entity.name] = entity

    def add_overlay(self, entity: Entity):
        self.overlays.append(entity)

    def update(self, dt: float, manager: Manager):
        for e in self._all_live_entities():
            e.update(dt, manager)
            if e.dead:
                self._remove(e)

    def _remove(self, entity: Entity):
        for l in self._all_lists():
            try:
                l.remove(entity)
            except ValueError:
                # fine probably
                pass
        if entity.name is not None:
            del self.names[entity.name]

    def render(self, canvas: Surface, camera: Camera):
        canvas.fill(self.bg_color)
        for e in self._all_live_entities():
            e.render(canvas, camera)

    def set_bg(self, bg_color):
        self.bg_color = bg_color
