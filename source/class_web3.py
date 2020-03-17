import time

from web3 import Web3

from source.methods_json import load_json

class Web3Connection(object):
    def __init__(self, network_url, abi, contract_address, wallet_private_key, w3 = None, contract = None, account = None):
        super().__init__()

        self.network_url = network_url
        self.abi = abi
        self.contract_address = contract_address
        self.wallet_private_key = wallet_private_key
        self.intitialize()

    def intitialize(self):
        # Connect to specific network
        self.w3 = Web3(Web3.HTTPProvider(self.network_url))
        print(self.w3.isConnected())

        # Setting up contract with the needed abi (functions) and the contract address (for instantiation)
        self.contract = self.w3.eth.contract(abi = self.abi, address = self.contract_address)
        print(self.contract.address)

        # account to interact from
        self.account = self.w3.eth.account.privateKeyToAccount(self.wallet_private_key)
        print(self.account.address)

    def create_character(self, name, unit, race):

        # get nonce for txn input
        nonce = self.w3.eth.getTransactionCount(self.account.address)

        # get identifier for function input
        identifier = str(name + unit + race)

        # build transaction
        txn_dict = self.contract.functions.createRandomCharacter(
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

        signed_txn = self.w3.eth.account.signTransaction(txn_dict, self.wallet_private_key)

        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("send txn: " + txn_hash.hex())

        txn_receipt = None

        print("waiting for nodes to handle txn")
        time.sleep(30)
        print("requesting for receipt of txn")

        txn_receipt = self.w3.eth.getTransactionReceipt(txn_hash.hex())

        newcharacter = "added " + name + " a " + unit + " consist of " + race
        return {'status': newcharacter, 'txn_receipt': txn_receipt}

    def get_characters(self):
        # print all knwon characters of the given wallet_address
        characters = self.contract.functions.getCharactersByOwner(self.account.address).call()

        characterlist = []
        for i in characters:
            charlist = self.contract.functions.characters(i).call()
            idlist = [i]
            character = idlist + charlist
            characterlist += [character]

        return characterlist

    def create_event(self, characterId, description):
        """create an event for a specific character by sending input to the smart contract of cryptocharacter"""
        # get nonce for txn input
        nonce = self.w3.eth.getTransactionCount(self.account.address)

        # build transaction
        txn_dict = self.contract.functions.createEvent(
            characterId, 
            description
            ).buildTransaction({
            'nonce': nonce,        
            'gas': 1648900,
            'gasPrice': w3.toWei('1000000000', 'wei'),
            'chainId': 3,
            })
        print("build txn dict: " + str(txn_dict))

        signed_txn = self.w3.eth.account.signTransaction(txn_dict, self.wallet_private_key)

        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("send txn: " + txn_hash.hex())

        txn_receipt = None

        print("waiting for nodes to handle txn")
        time.sleep(30)
        print("requesting for receipt of txn")

        txn_receipt = self.w3.eth.getTransactionReceipt(txn_hash.hex())

        newevent = "added " + description
        return {'status': newevent, 'txn_receipt': txn_receipt}

    def get_events(self, characterId):
        """get all events for a specific character by sending input to the smart contract of cryptocharacter"""

        # get all knwon events of the given character
        events = self.contract.functions.getEventsByCharacter(characterId).call()

        history = []
        history += ["characterId: " + str(characterId)]
        for i in events:
            eventlist = self.contract.functions.events(i).call()
            idlist = [i]
            event = idlist + [eventlist]
            history += [event]

        return history