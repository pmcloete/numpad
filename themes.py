
from tkinter.constants import N


class Themes():
    def __init__(self):
    
        self.theme_list = {'grey':{'BACKGROUND': '#000000',
                             'TEXT': '#fff4c9',
                             'INPUT': '#7E7E7E',
                             'TEXT_INPUT': '#FFFFFF',
                             'SCROLL': '#c7e78b',
                             'BUTTON': ('white', '#7E7E7E'),
                             'PROGRESS': ('#7E7E7E', '#D0D0D0'),
                             'BORDER': 1,
                             'SLIDER_DEPTH': 0,
                             'PROGRESS_DEPTH': 0},
                           'blue':{'BACKGROUND': '#2b2d42',
                             'TEXT': '#f1faee',
                             'INPUT': '#7E7E7E',
                             'TEXT_INPUT': '#edf2f4',
                             'SCROLL': '#c7e78b',
                             'BUTTON': ('white', '#8d99ae'),
                             'PROGRESS': ('#7E7E7E', '#D0D0D0'),
                             'BORDER': 1,
                             'SLIDER_DEPTH': 0,
                             'PROGRESS_DEPTH': 0}}

    def _get_theme(self, selection='blue'):
        for k, v in self.theme_list.items():
            if selection == k:
                return v

        
