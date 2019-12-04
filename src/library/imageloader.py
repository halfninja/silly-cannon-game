from pygame import Surface, image
from typing import Dict

loaded_images: Dict[str, Surface] = dict()


def get_image(path: str) -> Surface:
    try:
        return loaded_images[path]
    except KeyError:
        loaded_images[path] = surface = image.load(path)
        return surface
