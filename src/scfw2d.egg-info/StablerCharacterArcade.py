import arcade
import arcade.gui
from arcade.gui import UIManager
from orjson import loads
from DefaultMainMenu import *
from Enums import anchorX, anchorY, UIPosition, SoundData, Converter
from dataclasses import dataclass

@dataclass
class Dialog:
	message: str
	sideObjects: tuple = ()
	extraEvents: tuple = ()

@dataclass
class Branch:
	dialogsList: list

class Chapter:
	def __init__(self, branchList: dict):
		self.branchList = branchList
		self.currentBranch = branchList["main"]
		self.dialogIndex = 0

	def goToBranch(self, branchName: str):
		self.currentBranch = branchList[branchName]
		self.dialogIndex = 0

	def getCurrentDialog(self) -> Dialog:
		return self.currentBranch.dialogsList[self.dialogIndex]

	def advanceDialogIndex(self):
		if (len(self.currentBranch.dialogsList) - 1) == self.dialogIndex:
			return
		self.dialogIndex += 1

	def getCurrentBranchLength(self) -> int:
		return len(self.currentBranch.dialogsList)

class StoryManager:
	def __init__(self, chapters: list):
		self.chapters: list = chapters
		self.chapterIndex: int = 0

	def getNow(self) -> Dialog:
		return self.chapters[self.chapterIndex].getCurrentDialog()

	def getNext(self) -> Dialog:
		self.chapters[self.chapterIndex].advanceDialogIndex()
		return self.chapters[self.chapterIndex].getCurrentDialog()

	def getCurrentChapterLength(self) -> int:
		return self.chapters[self.chapterIndex].getCurrentBranchLength()

	def advanceDialogIndex(self):
		self.chapters[self.chapterIndex].advanceDialogIndex()

WINDOW_INFO: dict = {'width': 800, 'height': 600, 'title': "Test!"}
storyList: StoryManager = StoryManager([Chapter(
	{"main":Branch(
		[Dialog("Hello world!"), Dialog("How are you"),
		Dialog("I'm fine, Thank you."), Dialog("Bye bye")
		])
	})
])
soundDataList: dict = {}

PROJECT_INFO: dict = {"name": "Game"}
GameViewInfo: dict = {
	"bgcolor": arcade.csscolor.CORNFLOWER_BLUE, 
	"mainTextPos": UIPosition(
		WINDOW_INFO["width"] / 2, WINDOW_INFO["height"] / 2, 
		anchorX.center, anchorY.center
	)
}

def addAudioData(key: str, data: SoundData):
	soundDataList[key] = data

def setWindowInfo(nWindowInfo: dict):
	WINDOW_INFO = nWindowInfo

def setGameName(gamename: str):
	PROJECT_INFO["name"] = gamename

def setGameViewBackgroundColor(color: tuple):
	GameViewInfo["bgcolor"] = color

def setMainTextPos(nTextPos: UIPosition):
	GameViewInfo["mainTextPos"] = nTextPos

class GameView(arcade.View):
	def __init__(self, mainTextPos: UIPosition=UIPosition(WINDOW_INFO["width"] / 2, WINDOW_INFO["height"] / 2, \
		anchorX.center, anchorY.center), \
		advanceDialogKey: arcade.key=arcade.key.ENTER):
		# Call the parent class and set up the window
		super().__init__()

		self.storyListLength = storyList.getCurrentChapterLength()
		unitConverter = Converter()
		self.mainTextPos = mainTextPos
		self.mainTextPos.x_anchor = unitConverter.anchorXtoString(self.mainTextPos.x_anchor)
		self.mainTextPos.y_anchor = unitConverter.anchorYtoString(self.mainTextPos.y_anchor)
		self.UIManager = UIManager()
		self.advanceDialogKey = advanceDialogKey

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

		currentStoryObject = storyList.getNow()
		arcade.draw_text(currentStoryObject.message, self.mainTextPos.x, self.mainTextPos.y, arcade.color.WHITE, font_size=18, anchor_x=self.mainTextPos.x_anchor, anchor_y=self.mainTextPos.y_anchor)

	def on_show(self):
		""" This is run once when switch to this view """
		arcade.set_background_color(GameViewInfo["bgcolor"])

		# Reset the viewport, necessary if we have a scrolling game and we need
		# to reset the viewport back to the start so we can see what we draw.
		arcade.set_viewport(0, WINDOW_INFO["width"] - 1, 0, WINDOW_INFO["height"] - 1)

	def on_key_press(self, key, modifiers):
		""" Called when a key have been pressed. """

		if key == self.advanceDialogKey:
			storyList.advanceDialogIndex()

IS_ARCADE_RUNNING:bool = False

def start():
	global window
	window = arcade.Window(WINDOW_INFO["width"], WINDOW_INFO["height"], WINDOW_INFO["title"])

def showDefaultMainMenuView(bgcolor: tuple=arcade.csscolor.DARK_SLATE_BLUE):
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

def showCustomView(classname):
	customView = classname()
	window.show_view(customView)
	customView.setup()
	if not IS_ARCADE_RUNNING:
		arcade.run()
