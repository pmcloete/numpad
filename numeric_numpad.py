import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import DEFAULT_BASE64_ICON, DEFAULT_BASE64_ICON_16_BY_16, ICON_BUY_ME_A_COFFEE, InputText, set_global_icon
from themes import Themes


class Numpad:
    """Creates a numpad"""

    def __init__(self):
        """Initialize the keypad"""
        #  GUI Instance
        self.gui = sg

        #  Button Attributes
        self.size_button = (5, 1)
        self.size_border_button = 2
        self.button_font = ('Menlo', 25)
        self.color_button = '6C6C6C'
        self.color_enter_button = '#d90429'

        #  Display Field Attributes
        self.display_font = ('Menlo', 25)
        self.display_size = (18, 1)
        self.current_value = ''

        #  Info Text Attributes
        self.info_text_font = ('Menlo', 8)

        #  Theme Attributes
        self.theme = Themes()
        self.gui.theme_add_new('Peter', self.theme._get_theme(selection='grey'))
        self.gui.theme('Peter')

        #  Icon
        self.icon_path = '/Users/peter/Library/Mobile Documents/com~apple~CloudDocs/PythonMain/projects/pysimplegui_numpad/assests/website_logo.png'
        #  Main Layout
        self.layout = [
            [self.gui.Input(key='-VALUE-', font=(self.display_font),
                            size=self.display_size)
             ], [
                self.gui.Text('© Peter Inc. 2021', pad=(6, 2), font=(
                    self.info_text_font), justification='left')
            ],
            [
                self.gui.Button('EXIT', font=(self.button_font),
                                size=(self.size_button)),
                self.gui.Button('AC', font=(self.button_font),
                                size=(self.size_button)),
                self.gui.Button('<', font=(self.button_font),
                                size=(self.size_button))
            ],
            [
                self.gui.Button('7', font=(self.button_font),
                                size=self.size_button),
                self.gui.Button('8', font=(self.button_font),
                                size=self.size_button),
                self.gui.Button('9', font=(self.button_font),
                                size=self.size_button)],
            [
                self.gui.Button('4', font=(self.button_font),
                                size=self.size_button),
                self.gui.Button(
                    '5', font=(self.button_font),
                    size=self.size_button),
                self.gui.Button('6', font=(self.button_font),
                                size=self.size_button)],
            [
                self.gui.Button('1', font=(self.button_font),
                                size=self.size_button),
                self.gui.Button('2', font=(self.button_font),
                                size=self.size_button),
                self.gui.Button('3', font=(self.button_font),
                                size=self.size_button)
            ],
            [
                self.gui.Button('0', font=(self.button_font),
                                size=(self.size_button)),
                self.gui.Button('.', font=(self.button_font),
                                size=(self.size_button)),
                self.gui.Button('->', font=(self.button_font), button_color=(self.color_enter_button),
                                size=(self.size_button))
            ]
        ]

        #  Create the window accordingly
        self.window = self.gui.Window(
            'Numpad', self.layout, no_titlebar=False, grab_anywhere=True,
            resizable=True, finalize=True, titlebar_background_color='#000000', icon=DEFAULT_BASE64_ICON)
        self.window_size = self.window.Size

    def main(self):
        """The main function"""

        #  Numbers for the event loop
        event_items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        #  To enable updating the text display
        count = 0
        while True:
            event, value = self.window.read()
            #  Close the program
            if event == self.gui.WIN_CLOSED or event == 'EXIT':
                break
            #  Check if the button pressed is in event_items
            if event in event_items:
                #  Add a 0 before if numbers < 1 are to be entered
                if event.startswith('.') and not self.current_value:
                    count += 2
                    self.current_value = '0' + self.current_value
                #  Make sure the duplicate decimals cannot be added
                if self.current_value.endswith('.') and event == '.':
                    continue
                self.current_value += event
                count += 1

            #  Clear the display
            if event == 'AC':
                self.current_value = ''
            #  Backspace
            if event == '<':
                count -= 1
            #  Return/ Send data to where it needs to go
            if event == '->':
                #  Send the data entered to wherever it needs to go
                self._data_send()
                self.current_value = ''
                count = 0
            #  No more data in the display, reset the count
            if count == 0:
                self.current_value = ''
                count = 0
            #  Update the display field on every pass
            self._update_display(count)

        #  Program exited
        self.window.close()

    def _update_display(self, count):
        """Update the text display for the values entered on the keypad"""
        if count >= 0:
            self.window['-VALUE-'].update(self.current_value[:count])
        else:
            self.window['-VALUE-'].update(self.current_value)

    def _data_send(self):
        """Send the data after '->' is pressed on the keypad"""
        if not self.current_value:
            pass  # No data entered
        else:
            # if self.current_value.startswith('.'):
            #     self.current_value = '0' + self.current_value
            print('data sent')
            print(self.current_value)


if __name__ == '__main__':
    numpad = Numpad()
    numpad.main()
