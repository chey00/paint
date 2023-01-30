from PySide6.QtWidgets import QLabel


class DrawWidget(QLabel):
    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)
