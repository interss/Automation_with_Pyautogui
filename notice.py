# Description: This script to alert and request information from the user
import pyautogui
from time import sleep
# alert uer
pyautogui.alert(text='Iniciando sua automação', title='Automação de login', button='OK')
# request user information
email = pyautogui.prompt(text='Digite seu e-mail', title='Informações Obrigatórias')
print(f'Você digitou: {email}')
# enter password
senha = pyautogui.password(text='Digite sua senha:', title='Informações Obrigatórias', mask='*')
print(senha)
# confirm whether or not something should happen
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='Confirmação', buttons=['Yes','No','Cancel'])
if resposta == 'Yes':
    print('Continuar automação!')
# go to the coordinate and paste data
    pyautogui.click(3515,808,duration=2)
    pyautogui.typewrite(email)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.typewrite(senha)
    sleep(1)

elif resposta == 'No':
    print ('Encerrando automação!')
else:
    print('Automação cancelada!')




