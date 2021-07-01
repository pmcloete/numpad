
from tkinter.constants import N


class Themes():
    def __init__(self):
        self.numpad_theme = {'BACKGROUND': '#000000',
                             'TEXT': '#fff4c9',
                             'INPUT': '#7E7E7E',
                             'TEXT_INPUT': '#FFFFFF',
                             'SCROLL': '#c7e78b',
                             'BUTTON': ('white', '#7E7E7E'),
                             'PROGRESS': ('#7E7E7E', '#D0D0D0'),
                             'BORDER': 1,
                             'SLIDER_DEPTH': 0,
                             'PROGRESS_DEPTH': 0}

    def _get_theme(self):

        return self.numpad_theme
