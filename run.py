import multiprocessing
import subprocess

# To run Jarvis
def startAlpha():
    try:
        import eel
        print("eel imported successfully in process 1")
    except ImportError:
        print("Error importing eel in process 1")

    # Code for process 1
    print("Process 1 is running.")
    from main import start
    start()

# To run hotword
def listenHotword():
    try:
        import eel
        print("eel imported successfully in process 2")
    except ImportError:
        print("Error importing eel in process 2")

    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startAlpha) 
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    subprocess.call([r'devices.bat'])
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")