import sys
import os

file_name = sys.argv[1]
for dir_ in ["compiled", "rendered"]:
    os.makedirs(dir_, exist_ok=True)
f = open(f"compiled/{file_name}.svg", "w")
class tag:
    def __init__(self, name, attrs=None):
        self._name = name
        self._attrs = " "+attrs if attrs else ""
    def add(self):
        f.write(f"<{self._name}{self._attrs} />")
    def __enter__(self, *_, **__):
        f.write(f"<{self._name}{self._attrs}>")
    def __exit__(self, *_, **__):
        f.write(f"</{self._name}>")
PAGEWIDTH_MM = 210
PAGEHEIGHT_MM = 297
f.write('<?xml version="1.0" encoding="UTF-8"?>')
with tag("svg", f'width="{PAGEWIDTH_MM}mm" height="{PAGEHEIGHT_MM}mm" version="1.1"'):
    XFOXES = 8
    foxwidth = PAGEWIDTH_MM / XFOXES
    for x in range(0, XFOXES):
        x = x * foxwidth
        YFOXES = 16
        foxheight = PAGEWIDTH_MM / XFOXES
        for y in range(0, YFOXES):
            y = y * foxheight
            tag("image", f'href="foxes/{file_name}" x="{x}mm" y="{y}mm" width="{foxwidth}mm" height="{foxheight}mm"').add()
