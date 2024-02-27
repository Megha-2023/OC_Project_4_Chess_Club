# Castle_Chess_Club

The project is an offline application of Chess Tournament Management for the Castle Club. The application is based on MVC(Model-View-Controller) pattern in python.

## Run the program

### 1. Create Virtual Environment

First, install virtualenv package of python and run following command on terminal:

```python
pip install virtualenv
python -m venv <<name_of_env>>
Windows: <<name_of_env>>\Scripts\activate.bat

Powershell: <<name_of_env>>\Scripts\activate

Unix/MacOS: source <<name_of_env>>/bin/acivate
```

### 2. Requirements

Secondly, copy requirements.txt file which contains the list of required libraries for this program.
Then run following command on terminal:

```python
pip install requirements.txt
```

### 3. Start the application

To start the application, run main.py file by running following command on terminal:

```python
python main.py
```

The application is menu-driven. Once the above command is entered Main Menu will be displayed on the command prompt. From Main Menu, you can navigate to different options to perform different operations.

### Main Menu

1. Tournament Menu: To enter into Tournament Menu to create, start or delete tournament.
2. Report Menu: To enter into Report Menu which will generate different reports.

### Tournament Menu

1. Create New Tournament
2. Check Existing Tournament

### Tournament SubMenu

1. Show Tournament Details
2. Add Players to the Tournament
3. Start Round
4. Show Results of the Tournament
5. Delete Tournament

### Report Menu

1. Show All Players
2. Show All Tournaments
3. Show name and dates of the given Tournament
4. Show list of players participating in given Tournament
5. Show All Rounds and Matches of the given Tournament

### Important

1. Number of Rounds are by default set to 4, which requires at least 8 players in the tournament
2. After each Round, players of the tournament are sorted by highest score.
3. Players are referenced by their unique National Chess ID.

### Flake8-html Report

A flake8 plugin generate HTML reports of flake8 violations. The reports will be stored in a folder flake8_html in the current directory.

```python
flake8 --format=html --htmldir=flake-report
```
