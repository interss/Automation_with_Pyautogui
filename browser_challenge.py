# Description: This script is used to open the browser and navigate to a specific URL
import webbrowser
from time import sleep
import pyautogui
# open the browser exisiting in the system
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(5)
# click in page
pyautogui.click(x=1134,y=253,duration=2)
# scroll the mouse to the position X,Y and click coordinate
pyautogui.scroll(-2515)
pyautogui.click()
# write name
pyautogui.write('My name')
sleep(1)
# click on the alert field
pyautogui.click(x=1146,y=286,duration=1)
sleep(1)
# click on the button OK
pyautogui.click(x=1709,y=241,duration=1)
sleep(1)
# up the page to the header
pyautogui.scroll(2515)
sleep(1)
# scrool until button download Excel and click button 
pyautogui.scroll(-3715)
sleep(1)    
pyautogui.click(x=1273,y=245,duration=1)
sleep(1)
# save file
pyautogui.click(x=1708,y=557,duration=1)
sleep(1)    
# click on the button download PDF
pyautogui.click(x=1255,y=391,duration=1)
sleep(1)    
# save file
pyautogui.click(x=1708,y=557,duration=1)
sleep(1)
# finish the automation
pyautogui.alert('The automation is finished')
sleep(1)
# close the browser
pyautogui.hotkey('ctrl','w')