# Description: This script to writing with special characters
import pyautogui
import pyperclip
# set function to sentence
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
# find coordinates, click and write
pyautogui.moveTo(59,165,duration=2)
pyautogui.click()
escrever_frase('Automação é incrível!')
