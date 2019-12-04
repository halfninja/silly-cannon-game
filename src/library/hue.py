import pygame
from typing import *
from library.types import *


class Hue:
    """
    Records a base hue for the screen, and keeps track of temporary
    hues for a fixed time. When that time elapses, it goes back to the base hue.
    Currently if a new hue is set while another one is in progress it will be
    completely replaced but an enhancement could be to track them all and blend
    the hues together.
    """
    def __init__(self, base_hue: Optional[Colorish]):
        self.timer: float = 0.0
        self.base_hue: Optional[Colorish] = base_hue
        self.hue: Optional[Colorish] = None

    def update(self, dt: float):
        """
        Update timers to expire any temporary hue.

        :param dt: time passed in seconds.
        """
        if self.timer > 0.0:
            self.timer -= dt
            if self.timer < 0.0:
                self.timer = 0.0

    def current_hue(self) -> Optional[Colorish]:
        """
        The currently active hue.
        """
        if self.timer == 0.0:
            return self.base_hue
        else:
            return self.hue

    def set_hue(self, hue: Colorish, time: float):
        self.hue = hue
        self.timer = time