import sys
import os

file_name = sys.argv[1]
for dir_ in ["compiled", "rendered"]:
    os.makedirs(dir_, exist_ok=True)
with open(f"compiled/{file_name}.svg", "w") as f:
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
    with tag("svg", f'width="{PAGEWIDTH_MM}mm" height="{PAGEHEIGHT_MM}mm" version="1.1" viewBox="0 0 {PAGEWIDTH_MM} {PAGEHEIGHT_MM}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'):
        with tag("defs"):
            XFOXES = 8
            foxwidth = PAGEWIDTH_MM / XFOXES
            YFOXES = 16
            foxheight = PAGEHEIGHT_MM / YFOXES
            with tag("pattern", f'id="foxPattern" patternUnits="userSpaceOnUse" width="{foxwidth}" height="{foxheight}"'):
                tag("image", f'xlink:href="{os.getcwd()}/foxes/{file_name}" width="{foxwidth}" height="{foxheight}" preserveAspectRatio="none"').add()
        tag("rect", f'width="100%" height="100%" fill="url(#foxPattern)"').add()

os.system(f"inkscape --export-type=png --export-filename=rendered/{file_name} --export-dpi=600 compiled/{file_name}.svg")
FOXES_BACK_INPUT = "foxes_back.svg"
FOXES_BACK_OUTPUT = "foxes_back.png"
if not os.path.exists(FOXES_BACK_OUTPUT):
    os.system(f"inkscape --export-type=png --export-filename={FOXES_BACK_OUTPUT} --export-dpi=300 {FOXES_BACK_INPUT}")
