from scfw2d.storybuilder import chapter, branch, dialog, build

def get_story():
    chapter("Chapter 1")
    branch("main")
    dialog("Hello world!")
    dialog("This is a test dialog built using the story builder.")
    return build()
