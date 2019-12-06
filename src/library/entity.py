from __future__ import annotations
from library import Renderable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from library import Manager


class Entity(Renderable):
    def __init__(self):
        self.dead = False

    def update(self, dt: float, manager: Manager): pass
