import os
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QUrl


class CountdownDialog(QDialog):

    def __init__(self, seconds: int, parent=None):

        super().__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'ui', 'countdown_dialog.ui')
        uic.loadUi(ui_path, self)

        self.seconds_left = seconds
        self.is_paused = False

        # Connect UI elements
        self.timer_label = self.findChild(QLabel, "timer_label")
        self.play_button = self.findChild(QPushButton, "play_button")
        self.reset_button = self.findChild(QPushButton, "reset_button")

        self.play_button.clicked.connect(self.toggle_pause)
        self.reset_button.clicked.connect(self.reset_timer)

        # Set up and start the countdown timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.timer_label.setText(self.format_time(self.seconds_left))

    def format_time(self, seconds: int) -> str:
        """
        Formats seconds into a DD HH MM SS string.

        Args:
            seconds (int): Number of seconds to format.

        Returns:
            str: Formatted time string.
        """
        d = seconds // 86400
        h = (seconds % 86400) // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{d:02d}d {h:02d}h {m:02d}m {s:02d}s"

    def update_time(self):
        """
        Decrements countdown timer and updates UI.
        Plays alarm when countdown reaches zero.
        """
        if not self.is_paused and self.seconds_left > 0:
            self.seconds_left -= 1
            self.timer_label.setText(self.format_time(self.seconds_left))

        if self.seconds_left == 0:
            self.timer.stop()
            self.timer_label.setText("Time's up!")
            self.play_sound()

    def play_sound(self):
        """
        Plays an alert sound when the countdown ends.
        """
        sound_path = os.path.join(os.path.dirname(__file__), 'assets', 'alarm2.wav')
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(sound_path))
        self.sound.setVolume(1.0)
        self.sound.play()

    def toggle_pause(self):
        """
        Toggles pause/resume state of the timer.
        """
        self.is_paused = not self.is_paused
        self.play_button.setText("Resume" if self.is_paused else "Pause")

    def reset_timer(self):
        """
        Resets (closes) the countdown dialog.
        """
        self.close()
