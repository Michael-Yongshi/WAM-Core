# Warhammer Army Manager (WAM)

An application in order to create, update, view and save your warband details for use in the Mordheim Warhammer world. Using this application there is no need anymore for manually calculating skills or looking up your warbands details, including references to all item, spells, abilities, etc. that are ingame and the rules governing engagements.

## Roadmap
- Adding calculation tables for use in battles, like hit tables, wound tables and injury tables
- Adding your own warband rules, items, abilities, etc. for use in more custom made games.
- Adding decorative events to warbands, characters and items, to individualize and decorate the achievements or special happening, including who you fought, who killed that huge rat ogre, etc.
- Add Killteam rules and mechanics

## Getting Started

## Development

The rest of these instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Python, IDE & Git

```
sudo apt install vscode
sudo apt install git # scm for windows
install python
install vscode - python extension
```

set git repository by entering "git clone"

set git url in the pop up

set git credentials by entering credentials in popup

set some git configurations first
```
git config --global user.email "" 
git config --global user.name ""
# git config --global submodule.recurse true
git submodule init
git submodule update
```

Remove deleted branches of local vs code instance
```
git fetch --prune
```

### Basic application requisites

Building a virtual environment
https://realpython.com/python-virtual-environments-a-primer/
```
pip3 install --user venv                # (unused) virtual environment
pip3 install --user flake8              # (unused) editor support
pip3 install --user flask               # (unused) web application development
```

### API requisites

```
pip3 install --user requests            # (unused) default api library
```

### Solidity requisites

#### WEB3:
library for interacting with ethereum, setting up connections and interacting with smart contracts

Visual 14 C++ needed
https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
select visual studio build tools 2017, only the first optional checkbox (windows 10 sdk for desktop c++)

only then with pip
```
pip3 install --user web3                # (prod) 
```

#### Solidity Compiler:
solidity compiler for windows (solc) - based on https://www.codeooze.com/blockchain/solc-hello-world/

Combinations:
- (current)             solidity compiler 0.6.2 and Open Zeppelin 3.0.0 Beta
- (needs adaptation)    solidity compiler 0.5.10 and Open Zeppelin 2.5.0

get windows zip for solidity compiler from:
https://github.com/ethereum/solidity/releases
info:
https://solidity.readthedocs.io/en/v0.6.2/
https://solidity.readthedocs.io/en/v0.5.10/

get open zeppelin zip release from:
https://github.com/OpenZeppelin/openzeppelin-contracts/releases/
for direct lookup of contracts
https://github.com/OpenZeppelin/openzeppelin-contracts/releases/tag/v3.0.0-beta.0
https://github.com/OpenZeppelin/openzeppelin-contracts/releases/tag/v2.5.0

Install solidity compiler:
-extract to any folder, but advised to appdata/roaming/

install open zeppelin release: 
-extract to any folder
-copy contracts content
-paste in contracts folder of git repo/source/contracts

To use
-cd to folder in cmd
-compile by running:
```
solc -o C:\Users\mfvan\Documents\Git\Warband_Manager\source\ethereum\build\build0510\ --optimize --overwrite --bin --abi --ast --asm C:\Users\mfvan\Documents\Git\Warband_Manager\source\ethereum\CryptoCharacter0510.sol
solc -o C:\Users\mfvan\Documents\Git\Warband_Manager\source\ethereum\build\build062\ --optimize --overwrite --bin --abi --ast-json --asm C:\Users\mfvan\Documents\Git\Warband_Manager\source\ethereum\CryptoCharacter062.sol
# I packaged the dependencies (basically all openzeppelin contracts) in the contracts folder in my git.
```

The artifacts are then dropped in a build-version- folder in source\ethereum\build.
- abi: interface of the specific contract
- bin: bytecode of the specific contract
- evm: EVM Assembly / Opcodes
- sol.ast: 

Solidity Contracts Merger
We try to combine our contract with all its dependencies using Solidity Contracts Merger(vs code extention)
We need it as the compiler doesn't merge the outputs of the smart contracts to a single bytecode and abi
however the merged contract is not compilable

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
solidity compiler for python on windows (currently not working; file not found error):
install nodejs and npm open npm command line exe
```
npm install -g solc
```

wrapper
https://pypi.org/project/py-solc/

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

get solidity standards dependencies from openzeppelin:
https://github.com/OpenZeppelin/openzeppelin-contracts
Copy the contracts folder in whole, or just the files we are using (retaining the path):
- contracts/token/ERC721/IERC721.sol
- contracts/token/ERC721/IERC721Receiver.sol
- contracts/introspection/ERC165.sol
- contracts/math/SafeMath.sol

### NFC through pyscard
Can only be used with version 3.6.8 of python (as of moment of writing). Thus we have to switch for this application to this python version in order to use this NFC library.
Downloaded pyscard executable for windows from https://sourceforge.net/projects/pyscard/
tutorial: https://pyscard.sourceforge.io/user-guide.html
other info:
https://stackoverflow.com/questions/56423316/i-can-not-understand-my-symptoms-python-is-using-pyscard
https://github.com/GPII/linux-rfid-user-listener/blob/master/scriptor.1p
https://khanhicetea.com/post/reading-nfc-card-id-on-ubuntu/#Source-code
https://stackoverflow.com/questions/34869625/how-to-read-or-write-smart-card

### Ethereum node with Raspbian and DappNode
Downlaod SD Formatter and Etcher flasher to format and flash SD drives

https://www.reddit.com/r/ethereum/comments/fo1p2b/ethereum_on_arm_nethermind_and_hyperledger_besu/
https://www.mycryptopedia.com/how-to-run-an-ethereum-node-on-a-raspberry-pi/

Install Raspbian instructions (download raspbian light for terminal version; also preferred for less problems with flashing):
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

make sure the r-pi is up to date
```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo reboot
```

switch to desktop
```
sudo apt install xserver-xorg           # Display core for linux
sudo apt install raspberrypi-ui-mods    # R-pi default, see other here: https://raspberrytips.com/upgrade-raspbian-lite-to-desktop/
sudo apt install lightdm                # should be installed automatically by the display package, then this code will do nothing
sudo reboot                             # reboot now
sudo shutdown -h now                    # shutdown now
```

XXXXXXXXXXXXXXXX
not working on 32 bit rpi2
Install dappnode instructions
https://github.com/dappnode/DAppNode/wiki/DAppNode-Installation-Guide#installation-via-installer-script

```
wget -qO - https://prerequisites.dappnode.io  | sudo bash   # Download prerequisites
wget -qO - https://installer.dappnode.io | sudo bash        # install dappnode
```

use openvpn client to connect to the node remotely:
https://github.com/dappnode/DAppNode/wiki/OpenVPN-Client-Guide#Windows


### Authentication requisites
https://realpython.com/token-based-authentication-with-flask/


## Running the tests



### Break down into end to end tests



### And coding style tests



## Deployment



## Built With



## Contributing



## Versioning



## Authors

* **Michael-Yongshi** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License



## Acknowledgments
