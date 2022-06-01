from re import findall

import pyautogui
import pyperclip
import pytesseract
import pytest
from PIL import Image

tests = [
    ('123*5-6', 609),
    ('4566/2-11', 2272),
    ('123-456+456', 125),
    ('456*2-21', 891)
]

controls = {
    '1': (100, 425),
    '2': (165, 425),
    '3': (235, 425),
    '-': (305, 425),
    '4': (100, 380),
    '5': (165, 380),
    '6': (235, 380),
    '*': (305, 380),
    '7': (100, 335),
    '8': (165, 335),
    '9': (235, 335),
    '/': (305, 335),
    '0': (100, 475),
    '.': (165, 475),
    '%': (235, 475),
    '+': (305, 475),
    '=': (370, 450),
    'backspace': (105, 285),
    'screen': (235, 220),
    'result': (80, 210)
}


def find_coord():
    print(pyautogui.position())


def delete():
    pyautogui.leftClick(*controls['backspace'])


def inputer():
    delete()
    return input('Print some expression:')


def parser(expression=''):
    if not expression:
        expression = inputer()
    for letter in expression:
        if letter == ' ':
            continue
        else:
            pyautogui.leftClick(*controls[letter])
    pyautogui.leftClick(*controls['='])


def printer(expression):
    delete()
    pyautogui.leftClick(*controls['screen'])
    parser(expression)


def copy_result() -> str:
    pyautogui.click(*controls['result'], clicks=2, interval=0.25)
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


@pytest.mark.parametrize("expression, result", tests)
def test_screenshot(expression, result):
    printer(expression)
    pyautogui.screenshot('1.png', region=(56, 186, 350, 65))
    fact_result = int(findall(r'\d+', pytesseract.image_to_string(Image.open('1.png')))[0])
    assert fact_result == result


if __name__ == '__main__':
    find_coord()
    # parser()
    # test_screenshot()
