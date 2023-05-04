from PyQt5.QtWidgets import *
from controller import *
def main():
    app = QApplication([])
    window = Controller ()
    window.show()
    app.exec_()


if __main__ == "__main__":
    main()