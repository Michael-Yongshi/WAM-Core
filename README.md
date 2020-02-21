# Warhammer Army Manager (WAM)

An application in order to create, update, view and save your warband details for use, including but not limited to, Mordheim and Killteam boardgames. Using this application there is no need anymore for manually calculating skills or looking up your warbands details, including references to all item, spells, abilities, etc. that are ingame.

In addition you can add your own warbands, items, rules, etc. for use in more custom made games.

## Roadmap

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

install vscode
install git scm
install python
install vscode - python extension

set git repository by entering "git clone"
set git url in the pop up
set git credentials by entering credentials in popup

set git name with git --global user.email ""
set git email with git --global user.name ""

pip3 install --user flake8 (dev)
pip3 install --user requests (unused)
pip3 install --user pyqt5
pip3 install --user pyinstaller (dev)

create normal distribution manually with 
        python -m PyInstaller cli.py --add-data "database/saves/cache.json";"database/saves/" --add-data "database/references/*.json";"database/references/" --icon="source\war_72R_icon.ico" --name WAM

create exe file manually with 
        <!-- python -m PyInstaller cli.py --add-data "database/saves/cache.json";"database/saves/" --add-data "database/references/*.json";"database/references/" --icon="source\war_72R_icon.ico" --name WAM_OF --onefile -->

create from spec with 
        python -m PyInstaller WAM.spec
        <!-- python -m PyInstaller WAM_OF.spec -->

Dist location:
        https://www.jottacloud.com/s/13030f55cae66fb428698777e670d3a052a

- Solidity stuff
        metamask network vincent: http://51.105.171.12
        https://ethereum.org/python/
```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

