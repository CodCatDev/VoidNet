import os
from pathlib import Path

os.environ['PYSDL2_DLL_PATH'] = str(Path(__file__).resolve().parent) + "\\libs"

import sdl2 as eng
import sdl2.ext as ext

class Window:
    def __init__(self, title: str, size: list[int]):
        self.title = title
        self.size = size
        self.events = []
        self.close = False
    def buildWindow(self):
        ext.init()
        window = ext.Window(title=self.title, size=self.size)
        window.show()
        self.window = window
    def upd(self):
        self.window.refresh()
    def updEvents(self):
        self.events = ext.get_events()
    def isClose(self):
        for event in self.events:
            if event.type == eng.SDL_QUIT:
                self.close = True
    def quit(self):
        self.window.close()
        ext.quit()