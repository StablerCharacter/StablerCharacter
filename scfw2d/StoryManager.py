from dataclasses import dataclass


@dataclass
class Dialog:
	message: str
	sideObjects: tuple = ()
	extraEvents: tuple = ()


@dataclass
class Branch:
	dialogs: list


class Chapter:
	def __init__(self, name: str, branches: dict):
		self.name = name
		self.branches = branches
		self.current_branch = branches["main"]
		self.dialog_index = 0

	def go_to_branch(self, branchName: str):
		self.current_branch = self.branches[branchName]
		self.dialog_index = 0

	def get_current_dialog(self) -> Dialog:
		return self.current_branch.dialogs[self.dialog_index]

	def advance_dialog_index(self):
		if (len(self.current_branch.dialogs) - 1) == self.dialog_index:
			return
		self.dialog_index += 1

	def get_current_branch_length(self) -> int:
		return len(self.current_branch.dialogs)


class StoryManager:
	def __init__(self, chapters: list):
		self.chapters: list = chapters
		self.chapter_index: int = 0

	def get_now(self) -> Dialog:
		return self.chapters[self.chapter_index].get_current_dialog()

	def get_next(self) -> Dialog:
		self.chapters[self.chapter_index].advance_dialog_index()
		return self.chapters[self.chapter_index].get_current_dialog()

	def get_current_branch_length(self) -> int:
		return self.chapters[self.chapter_index].get_current_branch_length()

	def advance_dialog_index(self):
		self.chapters[self.chapter_index].advance_dialog_index()
