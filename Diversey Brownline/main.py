from metra_gui import MetraGUI
import metra_data

metra_gui = MetraGUI(metra_data)

# Install pyinstaller and run the command below to create an exe for the app
# Also need to copy images folder to the exe root folder
# pyinstaller --onefile --noconsole -i <images/metra.ico> main.py