Countdown Timer

A simple and elegant countdown timer application built with Python and PyQt5. This application allows users to set a custom countdown duration (in days, hours, minutes, and seconds) and displays a running timer with pause/resume and reset functionality. An alarm sound plays when the countdown reaches zero.
Features

Set custom countdown durations using days, hours, minutes, and seconds.
Pause and resume the countdown timer.
Reset the timer to start over.
Visual timer display with a clean, modern UI.
Audio alert when the countdown finishes.
Cross-platform support (Windows, macOS, Linux).
Preview

Main Timer Window

[Main Timer Window](assets/main_window.png)

Countdown Dialog with Pause/Reset

[Countdown Dialog](assets/countdown_dialog.png)

Prerequisites
To run this application ensure you have the following installed:

Python 3.8 or higher
PyQt5 (pip install PyQt5)
Git (optional, for cloning the repository)

Installation
Follow these steps to set up and run the Countdown Timer:

Clone the repository:
git clone https://github.com/mahyarmohammadlou/CountdownTimer-.git
cd countdown-timer


Install dependencies:
pip install -r requirements.txt


Run the application:
python Countdown_Timer.py



Usage

Launch the application by running Countdown_Timer.py.
Enter the desired countdown duration using the input fields for days, hours, minutes, and seconds.
Click the Set button to start the countdown.
In the countdown dialog:
Click Pause/Resume to pause or resume the timer.
Click Reset to close the dialog and return to the main window.


An alarm sound will play when the countdown reaches zero.

Example
To set a countdown for 1 hour and 30 minutes:

Set Hours to 1 and Minutes to 30 in the main window.
Click Set to open the countdown dialog.
The timer will display 01h 30m 00s and count down in real-time.


Project Structure
countdown-timer/
├── assets/                 # Audio and image assets
│   └── alarm2.wav
├── ui/                    # UI files for PyQt5
│   ├── Countdown_Timer.ui
│   └── countdown_dialog.ui
├── Countdown_Timer.py     # Main application script
├── countdown_dialog.py    # Countdown dialog logic
├── requirements.txt       # Project dependencies
└── README.md              # This file

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your changes (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to your branch (git push origin feature-branch).
Create a Pull Request.

For more details, see CONTRIBUTING.md.
License
This project is licensed under the MIT License.
Contact
For questions, bug reports, or suggestions, please use GitHub Issues and feedback.     
Acknowledgments

PyQt5 for the GUI framework.
Python for its simplicity and versatility.
Thanks to the open-source community for inspiration and support.
