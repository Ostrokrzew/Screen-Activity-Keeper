# Screen-Activity-Keeper

Python script to keep screen active

## Requirements

* Python 3
* PyAutoGUI 0.9.53

Install all required modules:

```bash
pip install -r requirements.txt
```

## How to use

Open your favourite environment, install required modules and just run script for minimum functionality. See examples below.

### Example #1

Simple usage:

```bash
python ./screen_activity_keeper.py
```

### Example #2

Usage with mouse:

```bash
python ./screen_activity_keeper.py -m
```

or

```bash
python ./screen_activity_keeper.py --mouse
```

### Example #3

Usage with super focus on Microsoft Teams:

```bash
python ./screen_activity_keeper.py -p path/to/microsoft/teams/installation/Teams.exe
```

or

```bash
python ./screen_activity_keeper.py --teams-path path/to/microsoft/teams/installation/Teams.exe
```

### Example #4

Usage with super focus on Microsoft Teams and mouse:

```bash
python ./screen_activity_keeper.py -m -p path/to/microsoft/teams/installation/Teams.exe
```

or

```bash
python ./screen_activity_keeper.py --mouse --teams-path path/to/microsoft/teams/installation/Teams.exe
```

## Annotations

For MS Teams installation try checking "%LOCALAPPDATA%\Microsoft\Teams\current\Teams.exe".
