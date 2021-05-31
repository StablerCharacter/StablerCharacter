import arcade
import arcade.gui
from arcade.gui import UIManager
from orjson import loads
from traceback import print_exc
from DefaultMainMenu import *
import Enums

class Dialog:
	def __init__(self, message:str, sideObjects:tuple=(), extraEvents:tuple=()):
		self.message = message
		self.sideObjects = sideObjects
		self.extraEvents = extraEvents

class Branch:
	def __init__(self, dialogsList):
		self.dialogsList = dialogsList

class Chapter:
	def __init__(self, branchList:dict):
		self.branchList = branchList
		self.currentBranch = branchList["main"]
		self.dialogIndex = 0

	def goToBranch(self, branchName):
		self.currentBranch = branchList["branchName"]
		self.dialogIndex = 0

	def getCurrentDialog(self):
		return self.currentBranch.dialogsList[self.dialogIndex]

	def advanceDialogIndex(self):
		if (len(self.currentBranch.dialogsList) - 1) == self.dialogIndex:
			return
		self.dialogIndex += 1

global gconfig
global WINDOW_INFO
WINDOW_INFO:dict = {'width': 800, 'height': 600, 'title': "Test!"}
storyList:list = [Chapter(
	{"main":Branch(
		[Dialog("Hello world!"), Dialog("How are you"),
		Dialog("I'm fine, Thank you."), Dialog("Bye bye")
		])
	})
]
global PROJECT_INFO
PROJECT_INFO:dict = {"name": "Game"}
global GameViewInfo
GameViewInfo:dict = {"bgcolor": arcade.csscolor.CORNFLOWER_BLUE, "mainTextPos": {"x":{"x":WINDOW_INFO["width"] / 2, "anchor":Enums.anchorX.center}, "y":{"y":WINDOW_INFO["height"] / 2, "anchor":Enums.anchorY.center}}}

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

def setMainTextPos(nTextPos):
	GameViewInfo["mainTextPos"] = nTextPos

class GameView(arcade.View):
	def __init__(self, mainTextPos={"x":{"x":WINDOW_INFO["width"] / 2, "anchor":Enums.anchorX.center}, "y":{"y":WINDOW_INFO["height"] / 2, "anchor":Enums.anchorY.center}}):
		# Call the parent class and set up the window
		super().__init__()

		self.chapterIndex = 0
		self.storyListLenght = len(storyList[self.chapterIndex].currentBranch.dialogsList)
		self.unitConverter = Enums.Converter()
		self.mainTextPos = mainTextPos
		self.mainTextPos["x"]["anchor"] = self.unitConverter.anchorXtoString(self.mainTextPos["x"]["anchor"])
		self.mainTextPos["y"]["anchor"] = self.unitConverter.anchorYtoString(self.mainTextPos["y"]["anchor"])
		self.UIManager = UIManager()

	def setup(self):
		""" Setup the game here. Call this function to restart the game. """
		self.UIManager.purge_ui_elements()

		button = FlatButton("Next",
			onClickAction=lambda:self.on_key_press(arcade.key.ENTER, None),
			center_x=(WINDOW_INFO["width"] - 100),
			center_y=50, width=100, anchor_x="right", anchor_y="bottom")
		self.UIManager.add_ui_element(button)

	def on_draw(self):
		""" Render the screen. """

		arcade.start_render()

		currentStoryObject = storyList[self.chapterIndex].getCurrentDialog()
		arcade.draw_text(currentStoryObject.message, self.mainTextPos["x"]["x"], self.mainTextPos["y"]["y"], arcade.color.WHITE, font_size=18, anchor_x=self.mainTextPos["x"]["anchor"], anchor_y=self.mainTextPos["y"]["anchor"])

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(GameViewInfo["bgcolor"])

		# Reset the viewport, necessary if we have a scrolling game and we need
		# to reset the viewport back to the start so we can see what we draw.
		arcade.set_viewport(0, WINDOW_INFO["width"] - 1, 0, WINDOW_INFO["height"] - 1)

	def on_key_press(self, key, modifiers):
		""" Called when a key have been pressed. """

		if key == arcade.key.ENTER:
			storyList[self.chapterIndex].advanceDialogIndex()

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
	gameview = GameView(GameViewInfo["mainTextPos"])
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