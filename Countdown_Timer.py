import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QPushButton
from PyQt5 import uic
from countdown_dialog import CountdownDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), 'ui', 'Countdown_Timer.ui')
        uic.loadUi(ui_path, self)

        # Find input widgets by their object names
        self.days_spin = self.findChild(QSpinBox, "spinBox")
        self.hours_spin = self.findChild(QSpinBox, "spinBox_2")
        self.minutes_spin = self.findChild(QSpinBox, "spinBox_3")
        self.seconds_spin = self.findChild(QSpinBox, "spinBox_4")
        self.set_button = self.findChild(QPushButton, "pushButton")

        # Connect button click to handler
        self.set_button.clicked.connect(self.start_timer)

    def start_timer(self):
        """
        Calculates total time in seconds and opens the countdown dialog if valid.
        """
        total_seconds = (
                self.days_spin.value() * 86400 +
                self.hours_spin.value() * 3600 +
                self.minutes_spin.value() * 60 +
                self.seconds_spin.value()
        )

        if total_seconds > 0:
            self.hide()  # Hide main-window during countdown
            self.dialog = CountdownDialog(total_seconds, self)
            self.dialog.exec_()  # Block until dialog closes
            self.show()  # Show main-window again after count-down ends


if __name__ == "__main__":
    """
    Entry point of the application.
    Launches the main countdown setup window.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
