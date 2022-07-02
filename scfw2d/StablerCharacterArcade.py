import arcade
import arcade.gui
from arcade.gui import UIManager
from json import loads
from .DefaultMainMenu import *
from .StoryManager import Dialog, Branch, Chapter, StoryManager
from .Enums import anchorX, anchorY, UIPosition, SoundData, Converter
from typing import NoReturn


WINDOW_INFO: dict = {"width": 800, "height": 600, "title": "Test!"}
story_list: StoryManager = StoryManager([
	Chapter("Chapter 1", {
		"main": Branch([
			Dialog("Hello world!"),
			Dialog("This is a test dialog."),
			Dialog("Now that's all I have to say.")
		])
	})
])
sound_data_list: dict = {}

PROJECT_INFO: dict = {"name": "Game"}
game_view_info: dict = {
	"bgcolor": arcade.csscolor.CORNFLOWER_BLUE, 
	"main_text_pos": UIPosition(
		WINDOW_INFO["width"] / 2, WINDOW_INFO["height"] / 2, 
		anchorX.center, anchorY.center
	)
}

def add_audio_data(key: str, data: SoundData) -> NoReturn:
	sound_data_list[key] = data

def set_window_info(new_window_info: dict) -> NoReturn:
	WINDOW_INFO = new_window_info

def set_game_name(gamename: str) -> NoReturn:
	PROJECT_INFO["name"] = gamename

def set_game_view_background_color(color: tuple) -> NoReturn:
	game_view_info["bgcolor"] = color

def set_main_text_position(new_text_pos: UIPosition) -> NoReturn:
	game_view_info["main_text_pos"] = new_text_pos

def set_story(story: StoryManager) -> NoReturn:
	global story_list
	story_list = story


class GameView(arcade.View):
	def __init__(self, main_text_pos: UIPosition=UIPosition(WINDOW_INFO["width"] / 2, WINDOW_INFO["height"] / 2, \
		anchorX.center, anchorY.center), \
		advance_dialog_key: arcade.key=arcade.key.ENTER):
		# Call the parent class and set up the window
		super().__init__()

		self.story_list_length = story_list.get_current_branch_length()
		self.main_text_pos = main_text_pos
		self.main_text_pos.x_anchor = Converter.anchor_x_to_string(self.main_text_pos.x_anchor)
		self.main_text_pos.y_anchor = Converter.anchor_y_to_string(self.main_text_pos.y_anchor)
		self.manager = UIManager()
		self.manager.enable()
		self.advance_dialog_key = advance_dialog_key
		print(self.story_list_length)

	def setup(self):
		""" Setup the game here. Call this function to restart the game. """
		self.manager.clear()

		button = FlatButton("Next",
			on_click_action=lambda:self.on_key_press(arcade.key.ENTER, None),
			x=(WINDOW_INFO["width"] - 140),
			y=40, width=100, anchor_x="right", anchor_y="bottom")
		self.manager.add(button)

	def on_draw(self):
		""" Render the screen. """

		arcade.start_render()

		current_story_object = story_list.get_now()
		arcade.draw_text(
			current_story_object.message, 
			self.main_text_pos.x, 
			self.main_text_pos.y, 
			arcade.color.WHITE, 
			font_size=18, 
			anchor_x=self.main_text_pos.x_anchor, 
			anchor_y=self.main_text_pos.y_anchor
		)
		self.manager.draw()

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(game_view_info["bgcolor"])

		# Reset the viewport, necessary if we have a scrolling game and we need
		# to reset the viewport back to the start so we can see what we draw.
		arcade.set_viewport(0, WINDOW_INFO["width"] - 1, 0, WINDOW_INFO["height"] - 1)

	def on_key_press(self, key, modifiers):
		""" Called when a key have been pressed. """

		if key == self.advance_dialog_key:
			story_list.advance_dialog_index()

IS_ARCADE_RUNNING: bool = False

def start() -> NoReturn:
	global window
	window = arcade.Window(WINDOW_INFO["width"], WINDOW_INFO["height"], WINDOW_INFO["title"])

def show_default_main_menu_view(bgcolor: tuple=arcade.csscolor.DARK_SLATE_BLUE) -> NoReturn:
	main_menu_view = DefaultMainMenu(bgcolor, WINDOW_INFO, PROJECT_INFO, lambda: show_game_view())
	window.show_view(main_menu_view)
	main_menu_view.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()

def show_game_view() -> NoReturn:
	gameview = GameView(game_view_info["main_text_pos"])
	window.show_view(gameview)
	gameview.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()

def show_custom_view(classname) -> NoReturn:
	custom_view = classname()
	window.show_view(custom_view)
	custom_view.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()
