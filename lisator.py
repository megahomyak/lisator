import sys
import os
import json
import struct

dir_name = sys.argv[1]
for dir_ in ["compiled", "rendered"]:
    os.makedirs(f"{dir_}/{dir_name}", exist_ok=True)
PAGEWIDTH_MM = 210
PAGEHEIGHT_MM = 297
j = json.load(open(f"foxes/{dir_name}/pattern.json"))
cols = j["cols"]
rows = j["rows"]
del j
with open(f"foxes/{dir_name}/image.png", 'rb') as fhandle: # Stolen from https://stackoverflow.com/a/20380514
    head = fhandle.read(24)
    width, height = struct.unpack('>ii', head[16:24])
total_width_px = width*cols
dpi = total_width_px / (PAGEWIDTH_MM * 0.0393700787)
print(f"{dpi = }")
def generate(side):
    with open(f"compiled/{dir_name}/{side}.svg", "w") as f:
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
        f.write('<?xml version="1.0" encoding="UTF-8"?>')
        with tag("svg", f'width="{PAGEWIDTH_MM}mm" height="{PAGEHEIGHT_MM}mm" version="1.1" viewBox="0 0 {PAGEWIDTH_MM} {PAGEHEIGHT_MM}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'):
            if side == "back":
                tag("rect", f'width="100%" height="100%" fill="white"').add()
            with tag("defs"):
                foxwidth = PAGEWIDTH_MM / cols
                foxheight = PAGEHEIGHT_MM / rows
                with tag("pattern", f'id="foxPattern" patternUnits="userSpaceOnUse" width="{foxwidth}" height="{foxheight}"'):
                    imgpath = f"foxes/{dir_name}/image.png" if side == "front" else "sticker_back.svg"
                    preserveAspectRatio = "" if side == "back" else ' preserveAspectRatio="none"'
                    tag("image", f'xlink:href="{os.getcwd()}/{imgpath}" width="{foxwidth}" height="{foxheight}"{preserveAspectRatio}').add()
            tag("rect", f'width="100%" height="100%" fill="url(#foxPattern)"').add()
generate("front")
generate("back")

os.system(f"inkscape --export-type=png --export-filename=rendered/{dir_name}/front.png --export-dpi={int(dpi)} compiled/{dir_name}/front.svg")
os.system(f"inkscape --export-type=png --export-filename=rendered/{dir_name}/back.png --export-dpi=300 compiled/{dir_name}/back.svg")
