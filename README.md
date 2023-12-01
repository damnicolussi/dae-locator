# DAE Locator
[![Static Badge](https://img.shields.io/badge/Open%20in%20Telegram-label?style=flat&logo=telegram&logoColor=blue&labelColor=%232C2C32&color=blue&link=t.me%2Fdaelocator)](https://t.me/daelocator_bot)
![Static Badge](https://img.shields.io/badge/OpenStreetMap-label?color=orange)
![GitHub Repo stars](https://img.shields.io/github/stars/damnicolussi/dae-locator?color=green)
![GitHub forks](https://img.shields.io/github/forks/damnicolussi/dae-locator?color=green)
![GitHub License](https://img.shields.io/github/license/damnicolussi/dae-locator)

 DAE Locator is a Telegram Bot in Python that helps you find the nearest defibrillator around you thanks to the data saved in OpenStreetMap.

 ## Table of Contents
- [DAE Locator](#dae-locator)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
    - [Preview](#preview)
    - [Available commands](#available-commands)
    - [Available languages](#available-languages)
  - [How to Install and Run the Project](#how-to-install-and-run-the-project)
    - [Use the Telegram Bot](#use-the-telegram-bot)
    - [Run the project locally](#run-the-project-locally)
  - [How to contribute](#how-to-contribute)
  - [Credits](#credits)

 ## Description
 The Bot uses the data saved in [OpenStreetMap](https://www.openstreetmap.org/) to find the nearest defibrillator around you, in an area of 1km.
 
 Thanks to [Overpass API](https://overpass-api.de/) we can create a query to retrieve the defibrillators around the user position (latitude, longitude) and with the coordinates obtained we can get the address with the Reverse Geoding of [Nominatim](https://nominatim.openstreetmap.org/) and calculate the on foot road distance with [Project OSRM](https://project-osrm.org/). 

 ### Preview
 <p align="center"><img src="example/example.gif" alt="example" width="200"/></p>

 ### Available commands
 ```
/start      starts the bot
/help       provides help
/report     report a missing DAE
```

### Available languages
Currently the bot is available in four different languages:<br>
:gb: English<br>
:it: Italian<br>
:de: German<br>
:fr: French<br>
:es: Spanish

 ## How to Install and Run the Project
 ### Use the Telegram Bot
 You can use the Telegram Bot searching **@daelocator_bot** or by clicking this link [t.me/daelocator_bot](https://t.me/daelocator_bot)

### Run the project locally
 Clone this repository and go to the `local` folder
 ```bash
git clone https://github.com/damnicolussi/dae-locator
cd dae-locator/local
 ```
 Set up the `.env` file with your bot token ([how to get the token](https://core.telegram.org/bots/features#botfather)):
 ```python
 TOKEN:'telegram_bot_token'
 ```
 Install the requirements
 ```bash
pip install -r requirements.txt
 ```
 Run the application
 ```bash
python app.py
 ```

## How to contribute
Since the project uses the data available in OpenStreetMap it's possibile that some DAEs may not be present in the map.

We are continuously working to gather as much data as possible to update the map and make this bot as useful and reliable as possible.

If you have found a public defibrillator not indicated on the map you can upload it on OpenStreetMap or you can report it by:
- Typing `/report` in the Telegram Bot
- Compiling this <a href="https://share-eu1.hsforms.com/1yJynPcprTIe1rzWPf14QSA2djdd8" target="_blank">survey</a>

Your report will be considered, and the DAE will be added to the map as soon as possible.

For more information about the project, contact <a href='mailto:dae-locator@nicolussi.dev' target='_blank'>dae-locator@nicolussi.dev</a>

## Credits
- [OpenStreetMap](https://www.openstreetmap.org/)
- [Overpass API](https://overpass-api.de/)
- [Nominatim](https://nominatim.openstreetmap.org/)
- [Project OSRM](https://project-osrm.org/)
