import time

from web3 import Web3
from solc import compile_source

from source.methods_json import load_file

# class CryptoCharacter(object):
#     """"""
#     def __init__(self, w3, contract):
        
    # set up w3 connection
w3 = Web3(Web3.HTTPProvider("http://51.105.171.12"))

# https://solidity.readthedocs.io/en/develop/using-the-compiler.html#compiler-input-and-output-json-description
# JSON input for solidity compiler of smart contract
# compiled_sol = compile_standard(
#     {
#         'language': 'Solidity',
#         'sources': {
#             'CryptoCharacter.sol':{
#                 'urls': ["cryptocharacter/contracts/CryptoCharacter.sol"],
#             },
#         },
#     })

# the needed abi functions for this contract
abi = load_file("cryptocharacter/build/", "cc_abi")

# # the needed bytecode of the contract
with open("cryptocharacter/build/cc_bytecode.bin", mode='r') as binfile: # b is important -> binary
    bytecode = binfile.read()

with open("cryptocharacter/contracts/CryptoCharacter.sol", mode='r') as contractfile: # b is important -> binary
    contract_code = contractfile.read()

# set up the contract based on the bytecode and abi functions
contract = w3.eth.contract(abi = abi, bytecode = bytecode)

# account to deploy from
wallet_private_key = "0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09"
account = w3.eth.account.privateKeyToAccount(wallet_private_key)

txn_dict = contract.constructor().buildTransaction({
        'from': account.address,
        'nonce': w3.eth.getTransactionCount(account.address),   
        'gas': 164890,
        'gasPrice': w3.toWei('1000000000', 'wei'),
        'chainId': 98052
        })

signed_txn = account.signTransaction(txn_dict)
txn_hash = contract.constructor()
txn_receipt = w3.eth.waitForTransactionReceipt(signed_txn.rawTransaction)

# Create contract instance based on the deployed smart contract
contract = w3.eth.contract(address = txn_receipt.contract_address, abi = abi)
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())


def create_character(name, unit, race):

    # get nonce for txn input
    nonce = w3.eth.getTransactionCount(wallet_address)

    # get identifier for function input
    identifier = "1"

    # build transaction
    txn_dict = contract.functions.createRandomCharacter(
        identifier, 
        name, 
        unit, 
        race
        ).buildTransaction({
        'nonce': nonce,        
        'gas': 164890,
        'gasPrice': w3.toWei('1000000000', 'wei'),
        'chainId': 98052,
        })
    print("build txn dict: " + str(txn_dict))

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print("send txn: " + txn_hash.hex())

    txn_receipt = None

    print("waiting for nodes to handle txn")
    time.sleep(30)
    print("requesting for receipt of txn")

    count = 0
    while txn_receipt is None and (count < 5):

        txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())

        count += 1

        time.sleep(1)

    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

    # return str(name + " " + unit + " " + race + " " + txn_hash.hex())

def get_characters(wallet_address):
    # print all knwon characters of the given wallet_address
    characters = contract.functions.getCharactersByOwner(wallet_address).call()
    print("character Ids: " + str(characters))

    characterlist = []
    for i in characters:
        charlist = contract.functions.characters(i).call()
        idlist = [i]
        character = idlist + charlist
        characterlist += [character]

    return characterlist

        # # Print all events of the character
        # events = contract.functions.getEventsByCharacter(i).call()
        # print(events)

        # for e in events:
        #     event = contract.functions.events(e).call()
        #     print(e)

    def create_event(characterId):
        """create an event for a specific character by sending input to the smart contract of cryptocharacter"""
        NotImplemented

    def get_events(characterId):
        """get all events for a specific character by sending input to the smart contract of cryptocharacter"""
        NotImplemented


if __name__ == "__main__":
    
    deploy_contract(wallet_address, wallet_private_key)

    newcharacter = create_character(
        name = "2", 
        unit = "3", 
        race = "4",
    )
    print("New character: " + str(newcharacter))

    # newevent = create_event(
    #     wallet_address = wallet_address,
    #     wallet_private_key = wallet_private_key,
    #     characterId = 1,
    #     description = "Something happened",
    # )

    characters = get_characters(
        wallet_address = wallet_address,
    )
    print("Character data: " + str(characters))

    # events = get_events(
    #     wallet_address = wallet_address,
    #     characterId = 1,
    # )
    # print(events)
