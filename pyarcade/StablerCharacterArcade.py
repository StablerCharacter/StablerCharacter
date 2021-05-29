import arcade
import arcade.gui
from arcade.gui import UIManager
from orjson import loads
from traceback import print_exc
from DefaultMainMenu import *

global gconfig
global WINDOW_INFO
WINDOW_INFO:dict = {'width': 800, 'height': 600, 'title': "Test!"}
storyList:list = ["Hello world!"]
global PROJECT_INFO
PROJECT_INFO:dict = {"name": "Game"}
global GameViewInfo
GameViewInfo:dict = {"bgcolor": arcade.csscolor.CORNFLOWER_BLUE}

try:
	f = open("sconfig.json", "r")
	gconfig = loads(f.read())
	f.close()
except FileNotFoundError:
	print("Configuration file not found. exiting...")
	print_exc()
except Exception:
	print_exc()

def setWindowInfo(nWindowInfo):
	WINDOW_INFO = nWindowInfo

def setGameName(gamename):
	PROJECT_INFO["name"] = gamename

def setGameViewBackgroundColor(color):
	GameViewInfo["bgcolor"] = color

class GameView(arcade.View):
	def __init__(self):
		# Call the parent class and set up the window
		super().__init__()

		self.storyIndex = 0

	def setup(self):
		""" Setup the game here. Call this function to restart the game. """
		pass

	def on_draw(self):
		""" Render the screen. """

		arcade.start_render()

		arcade.draw_text(storyList[self.storyIndex], WINDOW_INFO["width"] / 2, WINDOW_INFO["height"] / 2, arcade.color.WHITE, font_size=18, anchor_x="center")

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(GameViewInfo["bgcolor"])

		# Reset the viewport, necessary if we have a scrolling game and we need
		# to reset the viewport back to the start so we can see what we draw.
		arcade.set_viewport(0, WINDOW_INFO["width"] - 1, 0, WINDOW_INFO["height"] - 1)

global IS_ARCADE_RUNNING
IS_ARCADE_RUNNING:bool = False

def start():
	global window
	window = arcade.Window(WINDOW_INFO["width"], WINDOW_INFO["height"], WINDOW_INFO["title"])

def showDefaultMainMenuView(bgcolor=arcade.csscolor.DARK_SLATE_BLUE):
	mainMenuView = DefaultMainMenu(bgcolor, WINDOW_INFO, PROJECT_INFO, lambda: showGameView())
	window.show_view(mainMenuView)
	mainMenuView.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()

def showGameView():
	gameview = GameView()
	window.show_view(gameview)
	gameview.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()

def showCustomeView(classname):
	customView = classname()
	window.show_view(customView)
	customView.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()

if gconfig['startGameOnImport']:
	start()