from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from library.scene import Scene


class Manager:
    def __init__(self, scene: Scene):
        self.scene = scene
