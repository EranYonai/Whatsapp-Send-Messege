- Pyinstaller command for windows (11, py 3.10):
`pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/eyonai/Desktop/dan/Whatsapp-Send-Messege/appicon.ico" --name "windows11-freegull" --add-data "C:/Users/eyonai/Desktop/dan/Whatsapp-Send-Messege/Calander_Make_event.py;." --add-data "C:/Users/eyonai/Desktop/dan/Whatsapp-Send-Messege/Freegull_Logo.jpeg;." --hidden-import "googloe.auth" --hidden-import "google_auth_oauthlib" --hidden-import "googleapiclient" --hidden-import "babel.numbers" --hidden-import "googleapiclient.discovery"  "C:/Users/eyonai/Desktop/dan/Whatsapp-Send-Messege/main.py"``

-pyinstaller command for mac (14, py 3.10):
pyinstaller --noconfirm --onefile --windowed --icon "/Users/eranyonai/Desktop/dan-wh/Whatsapp-Send-Messege/appicon.ico" --add-data "/Users/eranyonai/Desktop/dan-wh/Whatsapp-Send-Messege/Calander_Make_event.py:." --add-data "/Users/eranyonai/Desktop/dan-wh/Whatsapp-Send-Messege/Freegull_Logo.jpeg:." --hidden-import "googloe.auth" --hidden-import "google_auth_oauthlib" --hidden-import "googleapiclient" --hidden-import "babel.numbers" --hidden-import "googleapiclient.discovery" "/Users/eranyonai/Desktop/dan-wh/Whatsapp-Send-Messege/main.py"