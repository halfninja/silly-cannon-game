import pygame
from gummworld.gameclock import GameClock
from locals import *
from library.camera import Camera
from library import imageloader
from library.hue import Hue
from cannon import Cannon
from settings import *


__author__: str = 'Nick'


def main():
    pygame.init()

    hue = Hue(None)

    fire_hue = (255, 255, 0)

    gutter = 10
    size = width, height = (400, 300)
    speed = Vector2(2.0, 2.0)
    pos = Vector2(0.0, 0.0)
    run = True
    fps_value = None
    camera = Camera()

    pygame.display.set_icon(pygame.image.load("data/intro_ball.gif"))

    screen: Surface = pygame.display.set_mode(size)
    canvas: Surface = pygame.Surface((width, height))
    pygame.display.set_caption("Cannons")
    gui: UIManager = UIManager((width, height), 'data/themes/quick_theme.json')

    font = pygame.font.SysFont(None, 36)

    text_hellothere = font.render("Hello there", 1, text_color)
    text_hellothere_pos = text_hellothere.get_rect()
    # text_hellothere_pos.y = height - 10 - text_hellothere_pos.height
    text_hellothere_pos.bottom = height - gutter
    text_hellothere_pos.x = gutter

    fire_rect = Rect((0, 0), (60, 40))
    fire_rect.right = width - gutter
    fire_rect.bottom = height - gutter*2 - 20
    fire_button = UIButton(relative_rect=fire_rect,
                            text='Fire',
                            manager=gui
                            )
    slider_x = UIHorizontalSlider(manager=gui,
                                relative_rect=Rect((gutter, height - 20 - gutter), (width - gutter*2, 20)),
                                start_value=45,
                                value_range=(100, 10)
                                )

    camera.pos.x = -40
    camera.pos.y = -width // 2

    cannon = Cannon()

    with open('data/level1.txt', 'r') as level1:
        data = level1.read().splitlines()

    def update_world(dt: float):
        nonlocal pos
        pos = pos + speed

        cannon.update(dt)
        camera.update(dt)
        hue.update(dt)

        gui.update(dt)

    def render(interpolation: float):
        canvas.fill(bg_color)
        cannon.render(canvas, camera)

        screen.blit(canvas, screen.get_rect())

        screen.fill((100, 100, 100), special_flags=pygame.BLEND_ADD)

        current_hue = hue.current_hue()
        if current_hue is not None:
            screen.fill(current_hue, special_flags=pygame.BLEND_MULT)

        canvas.blit(text_hellothere, text_hellothere_pos)

        if fps_value is not None:
            fps = font.render("%d" % fps_value, 1, text_color)
            screen.blit(fps, Rect((gutter, height - 100), (200, 200)))

        gui.draw_ui(screen)

        pygame.display.update()

    def pause_world():
        pass

    def every_second(dt: float):
        #print("%fs elapsed" % dt)
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
                if event.user_type == 'ui_button_pressed':
                    if event.ui_element == fire_button:
                        camera.jitter_amount = 5.0
                        hue.set_hue(fire_hue, 0.1)

            gui.process_events(event)


if __name__ == '__main__':
    main()
