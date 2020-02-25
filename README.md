# Warhammer Army Manager (WAM)

An application in order to create, update, view and save your warband details for use, including but not limited to, Mordheim and Killteam boardgames. Using this application there is no need anymore for manually calculating skills or looking up your warbands details, including references to all item, spells, abilities, etc. that are ingame.

In addition you can add your own warbands, items, rules, etc. for use in more custom made games.

## Roadmap

## Getting Started

To use the application see 'Installing'. The rest of these instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Grab the zip folder from: https://www.jottacloud.com/s/13030f55cae66fb428698777e670d3a052a. 

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
git --global user.email ""
```
set git email with 
```
git --global user.name ""
```

Install some required packages
```
pip3 install --user pyqt5
pip3 install --user requests    # (unused)
pip3 install --user flake8      # (dev)
pip3 install --user pyinstaller # (dev)
```


- Solidity stuff
metamask network: http://51.105.171.12

https://ethereum.org/python/

## Running the tests



### Break down into end to end tests



### And coding style tests



## Deployment

create a distribution manually: 
```
python -m PyInstaller cli.py --add-data "database/saves/cache.json";"database/saves/" --add-data "database/references/*.json";"database/references/" --icon="source\war_72R_icon.ico" --name WAM
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



