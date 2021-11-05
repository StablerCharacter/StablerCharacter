from dearpygui import core as guicore, simple as guisimple

class EditorTheme:
	Dark = "Dark"
	Dark2 = "Dark2"
	Light = "Light"
	Classic = "Classic"
	Gray = "Gray"
	DarkGray = "Dark Gray"
	Cherry = "Cherry"
	Purple = "Purple"
	Gold = "Gold"
	Red = "Red"

guicore.set_main_window_size(1280, 720)
guicore.set_theme(EditorTheme.Dark2)
guicore.set_main_window_title("Story Editor")
guicore.add_additional_font("Ubuntu-Light.ttf", 18)

class Editor:
	def __init__(self):
		with guisimple.window("Editor", width=1265, height=680):
			guisimple.set_window_pos("Editor", 0, 0)
			guicore.add_text("Story Editor")
			guicore.add_spacing(count=2)
			guicore.add_table("storyList", headers=["Index", "Message", "Side Objects", "Extra Events"])
			guicore.set_table_data("storyList", data=[["0", "Hello there!", "None", "None"], ["1", "Bye!", "None", "None"]])
		guicore.start_dearpygui()

def initializeEditor():
	print("Editor Initialize process started")
	Editor()

initializeEditor()