from PySide6.QtWidgets import QApplication
from windows.main_window import MainWindow
from function.my_timer import start_timer

if __name__ == "__main__":
    app = QApplication()
    mainw = MainWindow()
    mainw.show()
    # start_timer()
    app.exec()
