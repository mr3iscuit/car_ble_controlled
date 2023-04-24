import sys
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal

DEVICE = "/dev/rfcomm0"
BAUD_RATE = 9600
device = serial.Serial(DEVICE, BAUD_RATE)

class DirectionalUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.initUI()

    def initUI(self):
        # Set up the layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        hbox1 = QHBoxLayout()
        vbox.addLayout(hbox1)

        # Add a label for the up button
        upLabel = QLabel('Up')
        upLabel.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(upLabel)

        # Add the up button
        self.upButton = QPushButton('^')
        self.upButton.clicked.connect(self.upClicked)
        hbox1.addWidget(self.upButton)

        hbox2 = QHBoxLayout()
        vbox.addLayout(hbox2)

        # Add the left button
        self.leftButton = QPushButton('<')
        self.leftButton.clicked.connect(self.leftClicked)
        hbox2.addWidget(self.leftButton)

        # Add a label for the center button (unused)
        centerLabel = QLabel()
        centerLabel.setAlignment(Qt.AlignCenter)
        hbox2.addWidget(centerLabel)

        # Add the right button
        self.rightButton = QPushButton('>')
        self.rightButton.clicked.connect(self.rightClicked)
        hbox2.addWidget(self.rightButton)

        hbox3 = QHBoxLayout()
        vbox.addLayout(hbox3)

        # Add a label for the down button
        downLabel = QLabel('Down')
        downLabel.setAlignment(Qt.AlignCenter)
        hbox3.addWidget(downLabel)

        # Add the down button
        self.downButton = QPushButton('v')
        self.downButton.clicked.connect(self.downClicked)
        hbox3.addWidget(self.downButton)

        # Set the window properties
        self.setWindowTitle('Directional UI')
        self.setGeometry(100, 100, 250, 250)
        self.show()

    def upClicked(self):
        # Handle the up button click event
        print('Up button clicked')
        device.write(b"4\n")

    def downClicked(self):
        # Handle the down button click event
        print('Down button clicked')
        device.write(b"2\n")

    def leftClicked(self):
        # Handle the left button click event
        print('Left button clicked')
        device.write(b"1\n")

    def rightClicked(self):
        # Handle the right button click event
        print('Right button clicked')
        device.write(b"3\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DirectionalUI()
    sys.exit(app.exec_())

