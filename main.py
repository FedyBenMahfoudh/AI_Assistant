import eel
from engine.features import *
from engine.command import *

from engine.command import *
def start():
    eel.init('www')
    playAssistantSound()


    eel.start('index.html')

# eel.start('index.html',host='localhost',block="True")  # Or whichever file is your main HTML file
# os.system('start chrome.exe --app="http://127.0.0.1:8000/index.html"')
# eel.start('index.html',mode=None,host='localhost',block=True) 