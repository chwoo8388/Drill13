from pico2d import *
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_i
import game_framework
import game_world
from boy import Boy
from grass import Grass

item_select_image = None
show_item_select = False


def handle_events():
    global show_item_select

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            show_item_select = not show_item_select
        elif (event.type == SDL_KEYDOWN and show_item_select and
              event.key in (SDLK_0, SDLK_1, SDLK_2)):
            show_item_select = False
        else:
            boy.handle_event(event)



def init():
    global boy, item_select_image, show_item_select

    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    item_select_image = load_image('item_select.png')
    show_item_select = False



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if show_item_select:
        item_select_image.draw(400, 300)
    update_canvas()


def finish():
    global item_select_image

    game_world.clear()
    item_select_image = None
