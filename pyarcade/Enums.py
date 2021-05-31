""" Special/Extra Events """
from enum import Enum

class SideObjectEvents(Enum):
	ClickToContinue = 0
	ClickToChoose = 1 # Required Parameter: Choice Index

class NormalExtraEvents(Enum):
	CheckInput = 0 # Required Parameter: Check lambda
	DoubleButtonChoice = 1 # Required Parameter: Choice1 Action | Choice2 Action
	TripleButtonChoice = 2 # Required Parameter: Choice1 Action | Choice2 Action | Choice3 Action

""" Positioning """

class anchorX(Enum):
	left = 0
	center = 1
	right = 2

class anchorY(Enum):
	top = 0
	center = 0
	bottom = 1

class Converter:
	def __init__(self):
		pass

	def anchorXtoString(self, anchorx):
		if anchorx == anchorX.left:
			return "left"
		elif anchorx == anchorX.center:
			return "center"
		elif anchorx == anchorX.right:
			return "right"
		else:
			return anchorx

	def anchorYtoString(self, anchory):
		if anchory == anchorY.top:
			return "top"
		elif anchory == anchorY.center:
			return "center"
		elif anchory == anchorY.bottom:
			return "bottom"
		else:
			return anchory
