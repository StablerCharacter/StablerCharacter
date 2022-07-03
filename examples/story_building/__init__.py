from arcade import csscolor
import scfw2d
from .story import get_story

scfw2d.set_story(get_story())
scfw2d.set_game_name("Test Game")
scfw2d.set_game_view_background_color(csscolor.CORNFLOWER_BLUE)
scfw2d.start() # Setup the window
scfw2d.show_default_main_menu_view()