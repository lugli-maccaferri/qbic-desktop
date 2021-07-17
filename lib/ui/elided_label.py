from PySide6.QtCore import Qt
from PySide6.QtGui import QApplication, QLabel, QFontMetrics, QPainter

class MyLabel(QLabel):
    def paintEvent( self, event ):
        painter = QPainter(self)

        metrics = QFontMetrics(self.font())
        elided  = metrics.elidedText(self.text(), Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)