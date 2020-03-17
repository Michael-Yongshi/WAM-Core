from source.methods_json import (
    load_json,
)
from source.class_web3 import (
    Web3Connection,
)

def test_deploy(network_url, abi, bytecode, wallet_private_key):

    # setting up a connection for a new contract:
    w3c = Web3Connection.initialize(
        network_url=network_url,
        abi=abi,
        bytecode = bytecode,
        wallet_private_key=wallet_private_key,
    )

    return w3c

def test_interact(network_url, abi, contract_address, wallet_private_key):
    # setting up a connection for an existing contract
    w3c = Web3Connection.initialize(
        network_url=network_url,
        abi=abi,
        contract_address=contract_address,
        wallet_private_key=wallet_private_key,
    )

    return w3c
    
def test_read(w3c):

    characters = w3c.get_characters()
    print("Character data: " + str(characters))

    history = w3c.get_events(
        characterId = 0,
    )
    print("history: " + str(history))

def test_write(w3c):
    newcharacter = w3c.create_character(
        name = "Destroyers", 
        unit = "Sea Guards", 
        race = "High Elves",
    )
    print(f"New character: {str(newcharacter)}")

    newevent = w3c.create_event(
        characterId = 0,
        description = "Victory against 0xd04bAcA7ac336EadE692Fd8EDF1a66e4A7d74919",
    )
    print(f"New event: {str(newevent)}")

if __name__ == '__main__':
    
    # some inputs for testing
    network_url = "https://ropsten.infura.io/v3/313b66f4d09a48feaa2ad6e73859464e"
    wallet_private_key = "0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09"
    abi = load_json("source/", "methods_eth_abi")
    contract_address="0x9435cFB566b87e22d9EB08E98EACa95cc2BF1420"
    bytecode = "source/methods_eth_bytecode.txt"

    # w3c = test_deploy(network_url=network_url, abi=abi, bytecode=bytecode, wallet_private_key=wallet_private_key)
    w3c = test_interact(network_url=network_url, abi=abi, contract_address=contract_address, wallet_private_key=wallet_private_key)

    # test_write(w3c)
    test_read(w3c)


