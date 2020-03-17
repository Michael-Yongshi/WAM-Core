from source.methods_json import (
    load_json,
)
from source.class_web3 import (
    Web3Connection,
)

if __name__ == '__main__':

    # # the needed bytecode of the contract
    with open("source/methods_eth_bytecode.txt", mode='r') as infile:
        bytecode = infile.read()

    w3c = Web3Connection.initialize(
        network_url="https://ropsten.infura.io/v3/313b66f4d09a48feaa2ad6e73859464e",
        abi=load_json("source/", "methods_eth_abi"),
        bytecode = bytecode,
        wallet_private_key="0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09",
    )

    # newcharacter = w3c.create_character(
    #     name = "Destroyers", 
    #     unit = "Sea Guards", 
    #     race = "High Elves",
    # )
    # print("New character: " + str(newcharacter))

    characters = w3c.get_characters()
    print("Character data: " + str(characters))

    # newevent = w3c.create_event(
    #     characterId = 0,
    #     description = "Victory against 0xd04bAcA7ac336EadE692Fd8EDF1a66e4A7d74919",
    # )

    history = w3c.get_events(
        characterId = 0,
    )
    print("history: " + str(history))