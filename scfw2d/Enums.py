from enum import Enum
from dataclasses import dataclass

""" Music & Sounds """
@dataclass
class SoundData:
	file_name: str
	volume: float = 1.0
	pan: float = 1.0
	loop: bool = False
	streaming: bool = False

""" Special/Extra Events """
class SideObjectEvents(Enum):
	ClickToContinue = 0
	ClickToChoose = 1 # Required Parameter: Choice Index

class NormalExtraEvents(Enum):
	GetInput = 0 # Required Parameter: [None]
	Choices = 1 # Required Parameter: Choice count | Actions

class GetInput:
	def __init__(self, callback):
		self.callback = callback

@dataclass
class Choices:
	choiceCount: int
	actions: list

""" Positioning """

class anchorX(Enum):
	left = 0
	center = 1
	right = 2

class anchorY(Enum):
	top = 0
	center = 1
	bottom = 2

@dataclass
class UIPosition:
	x: float
	y: float
	x_anchor: anchorX
	y_anchor: anchorY

class Converter:
	def __init__(self):
		pass

	@staticmethod
	def anchor_x_to_string(anchorx: anchorX):
		if anchorx == anchorX.left:
			return "left"
		if anchorx == anchorX.center:
			return "center"
		if anchorx == anchorX.right:
			return "right"

	@staticmethod
	def anchor_y_to_string(anchory: anchorY):
		if anchory == anchorY.top:
			return "top"
		if anchory == anchorY.center:
			return "center"
		if anchory == anchorY.bottom:
			return "bottom"
