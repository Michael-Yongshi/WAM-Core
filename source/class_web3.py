import time

from web3 import Web3

from source.methods_json import load_json

class Web3Connection(object):
    def __init__(self, w3, contract, account):
        super().__init__()
        self.w3 = w3
        self.contract = contract
        self.account = account
        
    @staticmethod
    def interact(network_url, abi, contract_address, wallet_private_key):

        # Connect to specific network
        w3 = Web3(Web3.HTTPProvider(network_url))
        print(w3.isConnected())

        # Setting up contract with the needed abi (functions) and the contract address (for instantiation)
        contract = w3.eth.contract(abi = abi, address = contract_address)
        print(contract.address)

        # account to interact from
        account = w3.eth.account.privateKeyToAccount(wallet_private_key)
        print(account.address)

        return Web3Connection(
            w3 = w3,
            contract = contract,
            account = account,
        )

    @staticmethod
    def deploy(network_url, abi, bytecode, wallet_private_key):
        pass

        # self.w3 = Web3(Web3.HTTPProvider(self.network_url))

        # # # the needed bytecode of the contract
        # with open(self.bytecode, mode='r') as binfile: # b is important -> binary
        #     bytecode = binfile.read()

        # with open("cryptocharacter/contracts/CryptoCharacter.sol", mode='r') as contractfile: # b is important -> binary
        #     contract_code = contractfile.read()

        # # set up the contract based on the bytecode and abi functions
        # contract = w3.eth.contract(abi = abi, bytecode = bytecode)

        # account to deploy from
        # wallet_private_key = "0xad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09"
        # account = w3.eth.account.privateKeyToAccount(wallet_private_key)

        # txn_dict = contract.constructor().buildTransaction({
        #         'from': account.address,
        #         'nonce': w3.eth.getTransactionCount(account.address),   
        #         'gas': 164890,
        #         'gasPrice': w3.toWei('1000000000', 'wei'),
        #         'chainId': 3, 
        #         })

        # signed_txn = account.signTransaction(txn_dict)
        # txn_hash = contract.constructor()
        # txn_receipt = w3.eth.waitForTransactionReceipt(signed_txn.rawTransaction)

        # # Create contract instance based on the deployed smart contract
        # contract = w3.eth.contract(address = txn_receipt.contract_address, abi = abi)
        # txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())


        # if __name__ == "__main__":
            
        # deploy_contract(wallet_address, wallet_private_key)

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

        newcharacter = f"added {name} a {unit} consist of {race}"
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