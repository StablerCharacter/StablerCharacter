""" StablerCharacter Arcade - Controller Script builder tool """

import wx

class StoryEditorDialog(wx.Dialog):
	def __init__(self, parent, title="Story editor"):
		super(StoryEditorDialog, self).__init__(parent, title=title, size=(600, 400))

class ApplicationPanel(wx.Panel):
	def __init__(self, parent):
		super(ApplicationPanel, self).__init__(parent)

		self.bfontObj = wx.Font(12, wx.MODERN, wx.BOLD, wx.BOLD, False, "Segoe UI")
		self.nfontObj = wx.Font(11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, "Segoe UI")
		self.smallerNFontObj = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, "Segoe UI")

		self.title = wx.StaticText(self, label="SCArcade - Script Builder tool", pos=(20, 15))
		self.title.SetFont(self.bfontObj)
		
		self.projectNameEntryLabel = wx.StaticText(self, label="Project name", pos=(25, 47))
		self.projectNameEntryLabel.SetFont(self.nfontObj)
		self.projectNameEntry = wx.TextCtrl(self, pos=(175, 45))
		
		self.startViewDropdownLabel = wx.StaticText(self, label="Start view", pos=(25, 82))
		self.startViewDropdownLabel.SetFont(self.nfontObj)
		self.startViewDropdown = wx.ComboBox(self, pos=(175, 80), choices=["Default Main Menu", "Game view", "Custom view"])
		self.startViewDropdown.SetFont(self.smallerNFontObj)
		
		# Main game view Text positioning Entry
		self.mainGameViewTextPosEntryInfoLabel = wx.StaticText(self, label="X                      Y", pos=(190, 115))
		self.mainGameViewTextPosEntryInfoLabel.SetFont(self.smallerNFontObj)
		self.mainGameViewTextPosEntryLabel = wx.StaticText(self, label="Story Text Position", pos=(25, 142))
		self.mainGameViewTextPosEntryLabel.SetFont(self.nfontObj)
		self.mainGameViewTextPosXEntry = wx.SpinCtrl(self, pos=(175, 140), value=str(800 / 2), min=0, max=800)
		self.mainGameViewTextPosXEntry.SetFont(self.smallerNFontObj)
		self.mainGameViewTextPosYEntry = wx.SpinCtrl(self, pos=(275, 140), value=str(600 / 2), min=0, max=600)
		self.mainGameViewTextPosYEntry.SetFont(self.smallerNFontObj)
		self.mainGameViewTextPosAnchorInputInfoLabel = wx.StaticText(self, label="Anchor", pos=(25, 172))
		self.mainGameViewTextPosAnchorInputInfoLabel.SetFont(self.smallerNFontObj)
		self.mainGameViewTextPosXAnchor = wx.ComboBox(self, pos=(174, 170), choices=["Left", "Center", "Right"])
		self.mainGameViewTextPosXAnchor.SetFont(self.smallerNFontObj)
		self.mainGameViewTextPosYAnchor = wx.ComboBox(self, pos=(274, 170), choices=["Top", "Center", "Bottom"])
		self.mainGameViewTextPosYAnchor.SetFont(self.smallerNFontObj)
		self.autoCalculatePositionCheckbox = wx.CheckBox(self, size=(300, 40), label="Auto calculate position to be in the center", pos=(25, 195))
		self.autoCalculatePositionCheckbox.SetFont(self.smallerNFontObj)
		self.autoCalculatePositionCheckbox.Bind(wx.EVT_CHECKBOX, self.autoCalculatePosCheckboxChange)

		# Window size input
		self.windowResolutionEntryLabel = wx.StaticText(self, label="Window Resolution", pos=(25, 242))
		self.windowResolutionEntryLabel.SetFont(self.nfontObj)
		self.windowResolutionXEntry = wx.SpinCtrl(self, pos=(175, 240), value="800", min=640, max=7680)
		self.windowResolutionXEntry.Bind(wx.EVT_SPINCTRL, self.calculateCenter)
		self.windowResolutionXEntry.SetFont(self.smallerNFontObj)
		self.windowResolutionXLabel = wx.StaticText(self, label="x", pos=(245, 242))
		self.windowResolutionXLabel.SetFont(self.nfontObj)
		self.windowResolutionYEntry = wx.SpinCtrl(self, pos=(275, 240), value="600", min=480, max=4320)
		self.windowResolutionYEntry.Bind(wx.EVT_SPINCTRL, self.calculateCenter)
		self.windowResolutionYEntry.SetFont(self.smallerNFontObj)

		self.storyScriptingButton = wx.Button(self, label="Story editor...", pos=(25, 280))
		self.storyScriptingButton.SetFont(self.smallerNFontObj)
		self.storyScriptingButton.Bind(wx.EVT_BUTTON, self.openStoryEditor)

	def autoCalculatePosCheckboxChange(self, event):
		if self.autoCalculatePositionCheckbox.GetValue():
			self.mainGameViewTextPosXEntry.Enable(False)
			self.mainGameViewTextPosYEntry.Enable(False)
			self.mainGameViewTextPosXAnchor.Enable(False)
			self.mainGameViewTextPosYAnchor.Enable(False)
			self.mainGameViewTextPosXEntry.SetValue(int(self.windowResolutionXEntry.GetValue() / 2))
			self.mainGameViewTextPosYEntry.SetValue(int(self.windowResolutionYEntry.GetValue() / 2))
		else:
			self.mainGameViewTextPosXEntry.Enable(True)
			self.mainGameViewTextPosYEntry.Enable(True)
			self.mainGameViewTextPosXAnchor.Enable(True)
			self.mainGameViewTextPosYAnchor.Enable(True)

	def calculateCenter(self, event):
		self.mainGameViewTextPosXEntry.SetMax(self.windowResolutionXEntry.GetValue())
		self.mainGameViewTextPosYEntry.SetMax(self.windowResolutionYEntry.GetValue())
		if self.autoCalculatePositionCheckbox.GetValue():
			self.mainGameViewTextPosXEntry.SetValue(int(self.windowResolutionXEntry.GetValue() / 2))
			self.mainGameViewTextPosYEntry.SetValue(int(self.windowResolutionYEntry.GetValue() / 2))

	def openStoryEditor(self, event):
		self.storyEditor = StoryEditorDialog(self)
		self.storyEditor.Show()

class ApplicationFrame(wx.Frame):
	def __init__(self, parent, title):
		super(ApplicationFrame, self).__init__(parent, title=title, size=(500, 600))

		self.panel = ApplicationPanel(self)

class Application(wx.App):
	def OnInit(self):
		self.frame = ApplicationFrame(parent=None, title="SCArcade - Script builder tool")
		self.frame.Show()

		return True

app = Application()
app.MainLoop()