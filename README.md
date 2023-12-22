# Pyinstaller command for windows (11, py 3.10):
- add full path for files '.../'
`pyinstaller --noconfirm --onefile --windowed --icon ".../appicon.icon" --name "windows11-freegull" --add-data ".../Calander_Make_event.py;." --add-data ".../Freegull_Logo.jpeg;." --hidden-import "google.auth" --hidden-import "google_auth_oauthlib" --hidden-import "googleapiclient" --hidden-import "babel.numbers" --hidden-import "googleapiclient.discovery"  ".../main.py"`

# pyinstaller command for mac (14, py 3.10):
- add full path for files '.../'
`pyinstaller --noconfirm --onefile --windowed --icon ".../appicon.ico" --add-data ".../Calander_Make_event.py:." --add-data ".../Freegull_Logo.jpeg:." --hidden-import "googloe.auth" --hidden-import "google_auth_oauthlib" --hidden-import "googleapiclient" --hidden-import "babel.numbers" --hidden-import "googleapiclient.discovery" ".../main.py"`