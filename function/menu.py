from webbrowser import open
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


# 跳转到Bilibili
def toBilibili():
    open("https://space.bilibili.com/23949616", new=0, autoraise=True)

# 跳转到Github
def toGithub():
    open("https://github.com/JOZA-ORANGE/", new=0, autoraise=True)
