from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pygame import Surface
    from library import Camera


class Renderable:
    def render(self, canvas: Surface, camera: Camera): pass
