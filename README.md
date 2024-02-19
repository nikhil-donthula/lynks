# lynks - python scripts to open multipe links/URLs from a csv or excel file

*Tired of opening multiple links/URLs every day by clicking all your bookmarks in your browser? Worry not! Here are the scripts to reduce your load by a bit😜*

This module consists of 2 scripts

1. **open_links_multiple_windows** : Opens links/URLs from each sheet of an Excel file in separate Chrome windows across Linux and Windows.
2. **open_links_single_window** : Opens links/URLs from a CSV file in Chrome across Linux and Windows.

Prerequisites:

* Softwares to be installed: *python, chrome*
* Works only in windows and linux OS

### open_links_multiple_windows:

Opens links/URLs from each sheet of an Excel file in separate Chrome windows across Linux and Windows.

**How to execute?**

* clone the project

  ```
  git clone https://github.com/nikhil-donthula/lynks.git
  ```
* add all the links in csv file 'links.xlsx' which shoul be opened.
* add multiple sheets in the excel sheet to open those urls in single window.
* **Note**: if you use only one sheet in excel, all the links will be opened in same window in separate tabs.
* **Note**: in every sheet first row first column cell should be named as **'URL**'
* install the modules

  ```
   python -m pip install openpyxl
   python -m pip install webbrowser
   python -m pip install platform
   python -m pip install subprocess
  ```
* change directory to *open_links_multiple_windows* folder
  ```
  cd open_links_multiple_windows
  ```
* execute the 'open_links.py' file.

  ###### Windows:


  ```
  python open_links.py
  ```

  Linux:

  ```
  chmod +x open_links.py
  python3 open_links.py
  ```

*Oh Noo!!! I have to run a command to open my links/URLs?*😒 --- Dont Worry if this is your feeling. Lets make it more simple for us.

* Linux OS: 
  Execute the command
  ```
  chmod +x linux_shortcut_multi.sh
  ```
  Now when ever you want to open all the links in the excel sheet:
  Just right click on the *linux_shortcut_multi.sh* file and click *Run as a Program* from your Files explorer to open chrome browser with all the links present in the excel sheet

  Windows OS:
  ```
  
  ```

### open_links_single_window:

Opens links/URLs from a CSV file in Chrome across Linux and Windows.

**How to execute?**

* clone the project

  ```
  git clone https://github.com/nikhil-donthula/lynks.git
  ```
* add all the links in csv file 'links.csv' presnt in *open_links_single_window* folder
* change directory to *open_links_single_window* folder
  ```
  cd open_links_single_window
  ```
* install the modules

  ```
   python -m pip install csv
   python -m pip install webbrowser
   python -m pip install platform
   python -m pip install subprocess
  ```
* execute the 'open_links_csv.py' file.

  ###### Windows:


  ```
  python open_links_csv.py
  ```
  Linux:

  ```
  chmod +x open_links_csv.py
  python3 open_links_csv.py
  ```

*Oh Noo!!! I have to run a command to open my links/URLs?*😒 --- Dont Worry if this is your feeling. Lets make it more simple for us.

* Linux OS: 
  Execute the command
  ```
  chmod +x linux_shortcut_multi.sh
  ```
  Now when ever you want to open all the links in the csv sheet:
  Just right click on the *linux_shortcut_single.sh* file from your Files explorer and click *Run as a Program* to open chrome browser with all the links present in the csv file

  Windows OS:
  ```
  
  ```