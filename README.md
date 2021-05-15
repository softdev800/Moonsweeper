# Moonsweeper
Игровой приложения "Лунный Сапёр"

Initial setup:

```
pip3 install -r requirements.txt
pip3 install PyInstaller
pip3 install PyQt5 PyInstaller
pyinstaller --windowed --icon=images/bomb.ico --name Moonsweeper minesweeper.py
pyinstaller Moonsweeper.spec
```
