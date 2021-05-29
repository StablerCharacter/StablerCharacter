import arcade
from arcade.gui import UIManager

# Events
global PLAY_BUTTON_CLICKED
PLAY_BUTTON_CLICKED:bool = False
global QUIT_BUTTON_CLICKED
QUIT_BUTTON_CLICKED:bool = False

class FlatPlayButton(arcade.gui.UIFlatButton):
	def on_click(self):
		PLAY_BUTTON_CLICKED = True
		print("[EVENTLOG] Play button clicked")

class FlatQuitButton(arcade.gui.UIFlatButton):
	def on_click(self):
		raise SystemExit

class DefaultMainMenu(arcade.View):
	def __init__(self, bgcolor, windowInfo, projectInfo, playButtonAction):
		super().__init__()
		self.bgcolor = bgcolor
		self.WINDOW_INFO = windowInfo
		self.PROJECT_INFO = projectInfo
		self.UIManager = UIManager()
		self.playButtonAction = playButtonAction

	def setup(self):
		""" Setup this view. Call this function to re-initialize the menu."""
		self.UIManager.purge_ui_elements()

		button = FlatPlayButton("Play", center_x=(self.WINDOW_INFO["width"] / 2), center_y=(self.WINDOW_INFO["height"] / 2) + 20, width=225)
		self.UIManager.add_ui_element(button)
		# button = FlatPlayButton("Settings", center_x=(self.WINDOW_INFO["width"] / 2), center_y=(self.WINDOW_INFO["height"] / 2), width=225)
		# self.UIManager.add_ui_element(button)
		button = FlatQuitButton("Quit", center_x=(self.WINDOW_INFO["width"] / 2), center_y=(self.WINDOW_INFO["height"] / 2) - 60, width=225)
		self.UIManager.add_ui_element(button)

	def on_draw(self):
		arcade.start_render()

		# Displays the game name
		arcade.draw_text(self.PROJECT_INFO["name"], self.WINDOW_INFO["width"] / 2, self.WINDOW_INFO["height"] - 50, arcade.color.WHITE, font_size=20, anchor_y="top", anchor_x="center")

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(self.bgcolor)