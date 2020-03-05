# Warhammer Army Manager (WAM)

An application in order to create, update, view and save your warband details for use in the Mordheim Warhammer world. Using this application there is no need anymore for manually calculating skills or looking up your warbands details, including references to all item, spells, abilities, etc. that are ingame and the rules governing engagements.

## Roadmap
- Adding experience and skill tables for leveling up heroes and henchmen groups
- Adding calculation tables for use in battles, like hit tables, wound tables and injury tables
- Adding your own warband rules, items, abilities, etc. for use in more custom made games.
- Adding events to warbands, characters and items, to individualize and decorate the achievements or special happening, including who you fought, who killed that huge rat ogre, etc.
- Add Killteam rules and mechanics

## Getting Started

To use the application see 'Installing'. The rest of these instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Grab the zip folder from:

<b>Windows 10 64 bit</b>: https://www.jottacloud.com/s/13030f55cae66fb428698777e670d3a052a. 

<b>Ubuntu 18 64 bit</b>: https://www.jottacloud.com/s/130ab5742a54b87443a896a37062196affa.

Unzip the folder and run the exe file within.

### Prerequisites (dev only)

```
install vscode
install git scm
install python
install vscode - python extension
```

set git repository by entering "git clone"

set git url in the pop up

set git credentials by entering credentials in popup

set git name with 
```
git config --global user.email ""
```
set git email with 
```
git config --global user.name ""
```

Install some required packages for the application
```
pip3 install --user pyqt5
apt-get install python3 pyqt5   # (prod) if pip3 doesn't work

pip3 install --user requests    # (unused) default api library

pip3 install --user flake8      # (unused) editor support

pip3 install --user pyinstaller # (dev) to create an installer
```

Solidity specific stuff

Visual 14 C++ needed for web3
https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15

```
pip3 install --user py-solc             # (unused) solidity compiler for python

pip3 install --user pyethereum          # (unused) Ethereum Virtual Machine for python, to run your own node, but also some handy stuff like calculating address from private key

pip3 install --user web3                # (prod) library for interacting with ethereum, setting up connections, i.e. to your wallet in metamask, transferring tokens and interacting with smart contracts

pip3 install --user flask               # (unused)
pip3 install --user flask-restful       # (unused)
pip3 install --user flask-marschmallow  # (unused)
```

NFC specific stuff
```
pip3 install -U nfcpy                   # (prod) library to interact with nfc devices

```


## Running the tests



### Break down into end to end tests



### And coding style tests



## Deployment

create a distribution manually: 
```
python -m PyInstaller cli.py --add-data "database/saves/cache.json";"database/saves/" --add-data "database/references/*.json";"database/references/" --icon="source\war_72R_icon.ico" --name WAM-Win10-64

python -m PyInstaller cli.py --add-data "database/saves/cache.json":"database/saves/" --add-data "database/references/*.json":"database/references/" --icon="source\war_72R_icon.ico" --name WAM-Ubuntu18-64
```
<!-- python -m PyInstaller cli.py --add-data "database/saves/cache.json";"database/saves/" --add-data "database/references/*.json";"database/references/" --icon="source\war_72R_icon.ico" --name WAM_OF --onefile -->

create a distribution from spec with 
```
python -m PyInstaller WAM.spec
```
<!-- python -m PyInstaller WAM_OF.spec -->

## Built With



## Contributing



## Versioning



## Authors

* **Michael-Yongshi** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License



## Acknowledgments



