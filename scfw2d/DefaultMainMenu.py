import arcade
import arcade.gui
from .Enums import anchorX, anchorY, Converter

# Events
global PLAY_BUTTON_CLICKED
PLAY_BUTTON_CLICKED: bool = False
global QUIT_BUTTON_CLICKED
QUIT_BUTTON_CLICKED: bool = False

class FlatButton(arcade.gui.UIFlatButton):
	def __init__(self, text: str, x: int = 0, y: int = 0, width: int = 100, height: int = 40, align='center', on_click_action=None, id: str = None, style = None, **kwargs):
		super().__init__(
			text=text, 
			x=x, 
			y=y, 
			width=width, 
			height=height, 
			id=id, 
			style=style, 
			**kwargs
		)
		self.on_click_action = on_click_action

	def on_click(self, event: arcade.gui.UIOnClickEvent):
		if self.on_click_action is not None:
			self.on_click_action()

class DefaultMainMenu(arcade.View):
	def __init__(self, bgcolor: tuple, window_info: dict, project_info: dict, play_button_action, buttons_anchor: tuple = (anchorX.center, anchorY.center)):
		super().__init__()
		self.bgcolor = bgcolor
		self.WINDOW_INFO = window_info
		self.PROJECT_INFO = project_info
		self.manager = arcade.gui.UIManager()
		self.manager.enable()
		self.play_button_action = play_button_action
		self.buttons_anchor = buttons_anchor

	def switch_view(self):
		self.play_button_action()

	def setup(self):
		""" Setup this view. Call this function to re-initialize the menu."""
		self.manager.clear()

		buttons = arcade.gui.UIBoxLayout()
		button = FlatButton("Play", on_click_action=lambda: self.switch_view(), width=225)
		buttons.add(button.with_space_around(bottom=20))
		button = FlatButton("Quit", on_click_action=lambda: self.window.close(), width=225)
		buttons.add(button)
		self.manager.add(
			arcade.gui.UIAnchorWidget(
				anchor_x=Converter.anchor_x_to_string(self.buttons_anchor[0]),
				anchor_y=Converter.anchor_y_to_string(self.buttons_anchor[1]),
				child=buttons
			)
		)

	def on_draw(self):
		arcade.start_render()

		# Displays the game name
		arcade.draw_text(self.PROJECT_INFO["name"], self.WINDOW_INFO["width"] / 2, self.WINDOW_INFO["height"] - 50, arcade.color.WHITE, font_size=20, anchor_y="top", anchor_x="center")
		self.manager.draw()

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(self.bgcolor)