from CTA_gui import CTA_GUI
import CTA_data

CTA_app = CTA_GUI(CTA_data)

# Install pyinstaller and run the command below to create an exe for the app
# Also need to copy images folder to the exe root folder
# pyinstaller --onefile --noconsole -i <images/CTA.ico> main.py