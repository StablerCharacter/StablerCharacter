from typing import NoReturn
from .StoryManager import StoryManager

class MarkdownParser:
	def __init__(self) -> NoReturn:
		self.chapters: list = []
		self.branches: list = []
		self.dialogs: list = []

	def parse_file(self, file: str) -> StoryManager:
		with open(file, "r") as f:
			for i in f.readlines():
				self.parse_line(i)

		return StoryManager(chapters)

