# Project Title

IMDB Crawler App

## Getting Started

These instructions will explain the documents of the project, and their use.

### Prerequisites

```
- Python 3
```
### Documents in the Project
```
1) app_dc_bot.py: Main script of the project - contains the GUI and it's functions. Run it to open one window of the app.

2) chromedriver.exe: The driver used by selenium, please make sure that you have the right driver for your chrome version which can be checked 
typing chrome://version/ in your browser.

3) discord_crawler_class.py: Script containing the selenium crawler for Discord.

4) main_window.py: Contains the python code for the GUI created using PyQT5 and its QT Designer.

5) main_window.ui: The GUI file used inside the app_dc_bot.py script.

6) message_database.csv: Database containing the data of messages sent. Please be aware that any changes in the number of columns in this file 
would require adjusting the Send Message functionality present in the app_dc_bot.py script.

7) readme.md: This file.

8) requirements.txt: Txt file containing the packages used within the project, the installing of these 
packages can be made as instructed at the "Installing" section of this readme.

9) run_app_parallel.py: Script to run the app_dc_bot as many times as required.

10) token.txt: Token file containing the token used to login into Discord. Create as many token files as required, and select them when running the app.

11) token_login_script.txt: Token login script used within the discord_crawler_class.py in the login function.

12) user_manual.docx: Word document showcasing the app an it's uses.

13) users_not_to_send.csv: Database containing the username of users that will not receive the message. 
Any changes in the number of columns of this document would require changing the code of the send message function.

```

### Installing

Installing dependecies.

```
1) Install dependencies

$ pip install -r requirements.txt

```

### Running the project 

```
You have two options: 
1) Running the app_dc_bot.py file opens one app window.

2) Running run_app_parallel.py - choose the number of simultaneous windows to be opened.

```
