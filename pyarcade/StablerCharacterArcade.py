import arcade
import arcade.gui
from arcade.gui import UIManager
from orjson import loads
from traceback import print_exc

gconfig = None
global WINDOW_INFO
WINDOW_INFO = {'width': 800, 'height': 600, 'title': "Hello world", 'windowbg': arcade.color.BLACK}
storyList = ["Hello world!"]
inGameCharacters = 1
isGameRunning = False

try:
    f = open("sconfig.json", "r")
    gconfig = loads(f.read())
    f.close()
except FileNotFoundError:
    print("Configuration file not found. exiting...")
    print_exc()
except Exception:
    print_exc()

try:
    storyList = gconfig['storylist']
except KeyError:
    pass

def setWindowInfo(nWindowInfo):
    WINDOW_INFO = nWindowInfo

def setStoryList(nStoryList, characters=1):
    storyList = nStoryList
    inGameCharacters = characters

def setBackgroundColor(color):
    WINDOW_INFO['windowbg'] = color

class MainGameView(arcade.View):
    def __init__(self, storyList, inGameCharacters):
        super().__init__()
        self.storyList = storyList
        self.inGameCharacters = inGameCharacters
        self.storyIndex = 0
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.storyList[self.storyIndex], 240, 400, arcade.color.WHITE, 54)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.storyIndex += 1;

class MainGame(arcade.Window):
    def __init__(self):
        global WINDOW_INFO
        super().__init__(WINDOW_INFO['width'], WINDOW_INFO['height'], WINDOW_INFO['title'])
        self.index = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.text = "Hello world!"

    def setup(self):
        pass

    def getDialogIndex(self):
        return self.index

def start(runOnOtherThread=False):
    global isGameRunning
    if isGameRunning:
        raise RuntimeError("The game is already running.")
        return
    if not runOnOtherThread:
        global window
        window = MainGame()
        # mainView = MainGameView(storyList, inGameCharacters)
        arcade.run()
        isGameRunning = True
    else:
        from threading import Thread
        Thread(target=MainGame, daemon=True)
        isGameRunning = True

if gconfig['startGameOnImport']:
    start()