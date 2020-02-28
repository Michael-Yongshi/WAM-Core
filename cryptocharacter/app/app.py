import time

from web3 import Web3
from solc import compile_files

from methods_json import load_file


def create_cc(wallet_address, wallet_private_key, name, unit, race):

    # set up w3 connection
    w3 = Web3(Web3.HTTPProvider("http://51.105.171.12"))

    # the necessary contract address for this contract
    contract_address = "0x20589989d97b41ea6b9F748CEB4a17527CaA2C1a"

    # the needed abi functions for this contract
    abi = load_file("cryptocharacter/abi/", "cc_abi")

    # set up the contract based on the abi functions and the contract address
    contract = w3.eth.contract(address=contract_address, abi = abi)

    # print all knwon characters of the given wallet_address

    characters = contract.functions.getCharactersByOwner(wallet_address).call()
    print(characters)

    for i in characters:
        character = contract.functions.characters(i).call()
        print(character)

        events = contract.functions.getEventsByCharacter(i).call()
        print(events)

        for e in events:
            event = contract.functions.events(e).call()
            print(e)


        # nonce = w3.eth.getTransactionCount(wallet_address)

        # txn_dict = {
        #         'from': wallet_address,
        #         'to': contract_address,
        #         'value': 0,
        #         'gas': 100000,
        #         'gasPrice': w3.toWei('1000000000', 'wei'),
        #         'nonce': nonce,
        #         'chainId': 98052,
        # }

        # signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

        # txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # time.sleep(10)

        # txn_receipt = None
        # count = 0
        # while txn_receipt is None and (count < 5):

        #     txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())

        #     count += 1

        #     time.sleep(1)


        # if txn_receipt is None:
        #     return {'status': 'failed', 'error': 'timeout'}

        # return {'status': 'added', 'txn_receipt': txn_receipt}

    def create_event(characterId):
        """create an event for a specific character by sending input to the smart contract of cryptocharacter"""
        NotImplemented

    def get_events(characterId):
        """get all events for a specific character by sending input to the smart contract of cryptocharacter"""
        NotImplemented


if __name__ == "__main__":
    # set up w3 details
    mycharacter = create_cc(
        wallet_address = "0x980df35116009EB3937B0fD7931E3620114fDb9b",
        wallet_private_key = "0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09",
        name = "Michael", 
        unit = "Developer", 
        race = "Pikachu",
    )
    

    # create_event(
    #     characterId = 1,
    # )

    # get_events(
    #     characterId = 1,
    # )
