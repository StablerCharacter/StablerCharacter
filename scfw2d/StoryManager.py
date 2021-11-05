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
