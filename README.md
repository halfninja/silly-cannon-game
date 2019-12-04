# Silly Cannon Game

Playing around with Python, PyGame and `pygame-gui`. Work in progress.

## Installation

Have Python 3.7+ installed and on the path as `python` (or adjust the command below if it's `python3`). Then create a virtual environment to install the dependencies into, as below, so it doesn't mess with your system packages.

Note there might be an install error with the current version of `pygame-gui` where it requires `stringify` - if you get that then just `pip install stringify` for now.

    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements
    python src/main.py