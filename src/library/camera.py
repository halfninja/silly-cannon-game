import random

from locals import *
from typing import *
if TYPE_CHECKING:
    from library.manager import Manager


class Camera:

    def __init__(self):
        self.pos = Vector2(0.0, 0.0)
        self.jitter = Vector2(0.0, 0.0)
        self.jitter_amount = 0.0
        self.jitter_damp_factor = 0.90

    @property
    def x(self) -> float: return self.pos.x + self.jitter.x

    @property
    def y(self) -> float: return self.pos.y + self.jitter.y

    def update(self, _dt: float, _manager: 'Manager'):
        if self.jitter_amount == 0.0:
            self.jitter.x = 0.0
            self.jitter.y = 0.0
        else:
            self.jitter = Vector2(self._random_jitter(), self._random_jitter())
            self.jitter_amount *= self.jitter_damp_factor
            if self.jitter_amount < 0.1:
                self.jitter_amount = 0

    def _random_jitter(self) -> float:
        return random.uniform(-self.jitter_amount, self.jitter_amount)

    def translate(self, obj: Union[Vector2, Tuple[float, float]]):
        pass

    def get_rect(self, rect: Rect) -> Rect:
        """
        Call this on anything in the camera's scene before passing to render.
        It will apply any moving based on where the camera is.
        :param rect: A Rect in world space
        :return: A Rect in view space for blitting
        """
        return rect.move(int(-self.x), int(-self.y))
