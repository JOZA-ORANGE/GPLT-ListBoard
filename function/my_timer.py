from threading import Timer
from windows.main_window import MainWindow
import config
def autoRefresh():

    t = Timer(config.AutoRefreshTime, autoRefresh)
    t.start()

def start_timer():
    t = Timer(config.AutoRefreshTime, autoRefresh)
    t.start()