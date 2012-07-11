"""
SplitScreen-Resizer v1.0.0
by Jesus Leon
http://vizionika.net
http://iamjessu.com

A fork of:

SplitScreen v1.0.0
by Nick Fisher
https://github.com/spadgos/sublime-SplitScreen
"""
import sublime_plugin
import re


def addUp(lst):
    out = [0.0]
    for i in lst:
        out.append(out[-1] + i)

    return out


class SplitScreenResizerCommand(sublime_plugin.WindowCommand):
    def run(self, side):
        settings = view.settings()

        if side == "left":
            ratio = settings.get('ratio_left')
        else if side == "right":
            ratio = settings.get('ratio_right')


        """
        Keep original code in case we want to add vertical resizing.
        """
        parts = re.split("\\s*,\\s*", ratio)

        horiz = parts[0] or "1"
        vert = parts[1] or "1" if len(parts) > 1 else "1"

        vert = map(float, re.split(":", vert))
        horiz = map(float, re.split(":", horiz))
        vertTotal = sum(vert)
        horizTotal = sum(horiz)
        vert = map((lambda x: x / vertTotal), vert)
        horiz = map((lambda x: x / horizTotal), horiz)

        cols = addUp(horiz)
        rows = addUp(vert)

        cells = []
        for x, val1 in enumerate(horiz):
            for y, val2 in enumerate(vert):
                cells.append([x, y, x + 1, y + 1])

        self.window.run_command('set_layout', {
            "cols": cols,
            "rows": rows,
            "cells": cells
        })
