import time

from web3 import Web3
from solc import compile_source

from source.methods_json import load_file

# Connect to specific network
network_url = "https://ropsten.infura.io/v3/313b66f4d09a48feaa2ad6e73859464e"
w3 = Web3(Web3.HTTPProvider(network_url))
print(w3.isConnected())

# Setting up contract with the needed abi (functions) and the contract address (for instantiation)
abi = load_file("cryptocharacter/build/", "cc_abi")
contract_address = "0x4851Ef2081e2C799447017B4205dba0e4C8b0097"
contract = w3.eth.contract(abi = abi, address = contract_address)

# account to interact from
wallet_private_key = "0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09"
account = w3.eth.account.privateKeyToAccount(wallet_private_key)

def create_character(name, unit, race):

    # get nonce for txn input
    nonce = w3.eth.getTransactionCount(account.address)

    # get identifier for function input
    identifier = str(name + unit + race)

    # build transaction
    txn_dict = contract.functions.createRandomCharacter(
        identifier, 
        name, 
        unit, 
        race
        ).buildTransaction({
        'nonce': nonce,        
        'gas': 1648900,
        'gasPrice': w3.toWei('1000000000', 'wei'),
        'chainId': 3,
        })
    print("build txn dict: " + str(txn_dict))

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print("send txn: " + txn_hash.hex())

    txn_receipt = None

    print("waiting for nodes to handle txn")
    time.sleep(30)
    print("requesting for receipt of txn")

    txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())

    newcharacter = "added " + name + " the " + race + " from " + unit
    return {'status': newcharacter, 'txn_receipt': txn_receipt}

def get_characters():
    # print all knwon characters of the given wallet_address
    characters = contract.functions.getCharactersByOwner(account.address).call()
    print("character Ids: " + str(characters))

    characterlist = []
    for i in characters:
        charlist = contract.functions.characters(i).call()
        idlist = [i]
        character = idlist + charlist
        characterlist += [character]

    return characterlist

def create_event(characterId, description):
    """create an event for a specific character by sending input to the smart contract of cryptocharacter"""
    # get nonce for txn input
    nonce = w3.eth.getTransactionCount(account.address)

    # get identifier for function input


    # build transaction
    txn_dict = contract.functions.createEvent(
        characterId, 
        description
        ).buildTransaction({
        'nonce': nonce,        
        'gas': 1648900,
        'gasPrice': w3.toWei('1000000000', 'wei'),
        'chainId': 3,
        })
    print("build txn dict: " + str(txn_dict))

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print("send txn: " + txn_hash.hex())

    txn_receipt = None

    print("waiting for nodes to handle txn")
    time.sleep(30)
    print("requesting for receipt of txn")

    txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())

    newevent = "added " + description
    return {'status': newevent, 'txn_receipt': txn_receipt}

def get_events(characterId):
    """get all events for a specific character by sending input to the smart contract of cryptocharacter"""

    # print all knwon characters of the given wallet_address
    events = contract.functions.getEventsByCharacter(characterId).call()
    print("event Ids: " + str(events))

    history = []
    for i in events:
        history = contract.functions.events(i).call()
        idlist = [i]
        event = idlist + history
        history += [event]

    return history


if __name__ == "__main__":
    
    # newcharacter = create_character(
    #     name = "Destroyers", 
    #     unit = "Sea Guards", 
    #     race = "High Elves",
    # )
    # print("New character: " + str(newcharacter))

    # characters = get_characters()
    # print("Character data: " + str(characters))

    newevent = create_event(
        characterId = 3,
        description = "First battle",
    )

    history = get_events(
        characterId = 3,
    )
    print(history)
