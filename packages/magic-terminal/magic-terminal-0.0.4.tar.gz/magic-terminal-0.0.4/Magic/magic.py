import os
from typing import Optional, Union


class Style:
    default = '0'
    bright = '1'
    underlined = '4'
    blinking = '5'
    fixed_color = '7'


class Color:
    black = '30'
    red = '31'
    green = '32'
    yellow = '33'
    blue = '34'
    magenta = '35'
    cyan = '36'
    white = '37'
    reset = '\033[0m'


class Highlight:
    black = '40'
    red = '41'
    green = '42'
    yellow = '43'
    blue = '44'
    magenta = '45'
    cyan = '46'
    white = '47'


class Print:
    def text(text : str, style : Optional[Union[Style, str]] = Style.default, color : Optional[Union[Color, str]] = None, highlight : Optional[Union[Highlight, str]] = None, start_new_line : Optional[bool] = False, end_new_line : Optional[bool] = False):
        '''
            Print colored text.
        '''

        style = style if style else ''        
        start_new_line = '\n' if start_new_line else ''
        end_new_line = '\n' if end_new_line else ''
        
        os.system('')
        print(start_new_line + Get.layout(style, color, highlight) + text + Color.reset + end_new_line)

    def type(value):
        '''
            Print colored text based on the value type.
        '''

        color = {
            str: Color.red,
            int: Color.blue,
            bool: Color.yellow,
            float: Color.green,
            list: Color.magenta,
            dict: Color.cyan,
            tuple: Color.black,
            complex: Color.white,
            set: Color.white,
        }
        Print.text(str(value), None, color[type(value)])


class Get:
    def styled_text(text : str, style : Optional[Union[Style, str]] = Style.default, color : Optional[Union[Color, str]] = None, highlight : Optional[Union[Highlight, str]] = None):
        '''
            Get colored text.
        '''

        style = style if style else ''
        return Get.layout(style, color, highlight) + text + Color.reset

    def layout(style : Optional[Union[Style, str]] = Style.default, color : Optional[Union[Color, str]] = None, highlight : Optional[Union[Highlight, str]] = None):
        '''
            Get color object layout.
        '''

        style = style if style else ''
        color = ';' + color if color else ''
        highlight = ';' + highlight if highlight else ''

        return '\033[' + style + color + highlight + 'm'
