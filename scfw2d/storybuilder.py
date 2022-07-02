from .StoryManager import Dialog, Branch, Chapter, StoryManager
from typing import NoReturn

result: dict = {
    "dialogs": [],
    "branches": {},
    "chapters": []
}
context: dict = {}

def dialog(content: str = "") -> NoReturn:
    if "dialog" in context:
        result["dialogs"].append(context["dialog"])
    context["dialog"] = Dialog(content)

def branch(name: str = "") -> NoReturn:
    if "branch" in context:
        result["branches"][context["branch"]] = Branch(result["dialogs"])
        result["dialogs"] = []
    context["branch"] = name

def chapter(name: str = "") -> NoReturn:
    if "chapter" in context:
        result["chapters"].append(Chapter(context["chapter"], result["branches"]))
        result["branches"] = {}
    context["chapter"] = name

def build() -> StoryManager:
    dialog()
    branch()
    chapter()
    return StoryManager(result["chapters"])
