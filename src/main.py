from __future__ import annotations

import sys
from typing import *

import pygame

from cannon import Cannon
from gummworld import GameClock
from library.camera import Camera
from library.hue import Hue
from library.manager import Manager
from library.particles import Particles
from library.scene import Scene
from library import windows
from locals import *
from settings import *

__author__: str = 'Nick'

ScaleFactor = NewType("ScaleFactor", Literal[2, 3, 4, 5])


def main():
    windows.enable_hidpi_support()

    pygame.init()

    scale_factor: Literal[2, 3, 4, 5] = 3

    fire_hue = (255, 255, 0)

    gutter = 10
    width, height = (320, 240)
    screen_size = screen_width, screen_height = (width * scale_factor, height * scale_factor)
    gui_width, gui_height = screen_width, screen_height
    speed = Vector2(2.0, 2.0)
    pos = Vector2(0.0, 0.0)
    run = True
    camera = Camera()

    pygame.display.set_icon(pygame.image.load("data/intro_ball.gif"))

    screen: Surface = pygame.display.set_mode((screen_width, screen_height))
    canvas: Surface = pygame.Surface((width, height))
    pygame.display.set_caption("Cannons")
    gui: UIManager = UIManager((gui_width, gui_height), 'data/themes/quick_theme.json')

    fire_rect = Rect((0, 0), (60, 40))
    fire_rect.right = gui_width - gutter
    fire_rect.bottom = gui_height - gutter * 2 - 20
    fire_button = UIButton(relative_rect=fire_rect,
                           text='Fire',
                           manager=gui
                           )
    slider_x = UIHorizontalSlider(manager=gui,
                                  relative_rect=Rect((gutter, gui_height - 20 - gutter), (gui_width - gutter * 2, 20)),
                                  start_value=45,
                                  value_range=(100, 10)
                                  )

    camera.pos.x = -40
    camera.pos.y = -width // 2

    scene = Scene()
    scene.set_bg(bg_color)

    manager = Manager(scene)

    cannon = Cannon()
    scene.add(cannon)

    bullet_particles = Particles()
    bullet_particles.name = 'bullet_particles'
    scene.add(bullet_particles)

    hue = Hue(None)
    scene.add_overlay(hue)

    def update_world(dt: float):
        nonlocal pos
        pos = pos + speed

        scene.update(dt, manager)
        camera.update(dt, manager)

        gui.update(dt)

    def render(_interpolation: float):
        scene.render(canvas, camera)

        if scale_factor == 2:
            pygame.transform.scale2x(canvas, screen)
        else:
            pygame.transform.scale(canvas, screen_size, screen)

        gui.draw_ui(screen)
        pygame.display.update()

    def pause_world():
        pass

    def every_second(_dt: float):
        # print("%fs elapsed" % dt)
        pass

    clock = GameClock(
        update_callback=update_world,
        frame_callback=render,
        paused_callback=pause_world,
    )
    clock.schedule_interval(every_second, 1.0)

    while run:
        clock.tick()

        cannon.angle = slider_x.get_current_value()

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                elif event.key == K_SPACE:
                    camera.jitter_amount = 50.0
                else:
                    pass
            elif event.type == USEREVENT:
                if event.user_type == UI_BUTTON_PRESSED:
                    if event.ui_element == fire_button:
                        cannon.fire(manager)
                        camera.jitter_amount = 5.0
                        hue.set_hue(fire_hue, 0.1)

            gui.process_events(event)


if __name__ == '__main__':
    main()
