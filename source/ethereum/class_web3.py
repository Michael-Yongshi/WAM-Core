import os
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
    def initialize(network_url, wallet_private_key, abi, contract_address="", solidity="", bytecode=""):
        
        # Connect to specific network
        w3 = Web3(Web3.HTTPProvider(network_url))
        print(w3.isConnected())

        # account to interact from
        account = w3.eth.account.privateKeyToAccount(wallet_private_key)
        print(account.address)

        if contract_address == "" and bytecode == "" and solidity == "":

            print("provide valid contract address, solidity contract or bytecode to create a new contract!")

        else:

            if bytecode != "":
                # if bytecode is provided, create new contract (address) with provided bytecode
                contract_address = Web3Connection.init_deploy_bytecode(w3, account, abi, bytecode)

            elif solidity != "":
                # if solidity contract is provided, create new contract (address) with provided contract
                contract_address = Web3Connection.init_deploy_solidity(w3, account, abi, solidity)   
            
            # Setting up contract with the needed abi (functions) and the contract address (for instantiation)
            abi = load_json(abi["path"], abi["file"])
            # print(abi)
            
            contract = w3.eth.contract(abi = abi, address = contract_address)
            print(contract.address)

            return Web3Connection(
                w3 = w3,
                contract = contract,
                account = account,
            )

    @staticmethod
    def init_deploy_solidity(w3, account, abi, solidity):
        NotImplemented

        # relative_path = os.path.join("source", solidity)
        # current_directory = os.path.dirname(os.path.dirname(__file__))
        # absolute_path = os.path.join(current_directory, relative_path)

        # print(f"relative path {relative_path}")
        # print(f"absolute path {absolute_path}")

        # compile standard
        # compiled_sol = compile_standard(
        #     {"sources": absolute_path}
        # )

        # compile directly a sol file
        # compiled_sol = compile_files(absolute_path)

        # compile solidity source code
        # with open(relative_path, mode='r') as infile:
        #     source = infile.read()
        # compiled_sol = compile_source('pragma solidity ^0.4.0; contract A{ funcion A() public{}}')

    @staticmethod
    def init_deploy_bytecode(w3, account, abi, bytecode):
        """deploying a new contract with abi and bytecode"""

        # getting bytecode by opening the bytecode text file and save it as a string
        with open(bytecode, mode='r') as infile:
            bytecode = infile.read()

        # set up the contract based on the bytecode and abi functions
        contract = w3.eth.contract(abi = abi, bytecode = bytecode)

        # construct transaction
        txn_construct = contract.constructor().buildTransaction({
            'from': account.address,
            'nonce': w3.eth.getTransactionCount(account.address),
            'gasPrice': w3.toWei('10000000000', 'wei'),
            'chainId': 3, 
            }
        )
        # print(f"Constructed transaction: {txn_construct}") # Shows huge bit string

        # sign transaction
        txn_signed = account.signTransaction(txn_construct)
        # print(f"Signed transaction: {txn_signed}") # Shows huge bit string

        # send transaction
        txn_hash = w3.eth.sendRawTransaction(txn_signed.rawTransaction)
        print(f"Transaction send with hash: {txn_hash.hex()}")

        # wait for processing
        print("waiting for nodes to handle txn")
        time.sleep(60)

        # request receipt
        txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())
        print(f"Requested receipt: {txn_receipt}")

        # return new contract address
        new_contract_address = txn_receipt["contractAddress"]
        print(f"New contract address: {new_contract_address}\n")

        return new_contract_address

    def create_character(self, name, unit, race):

        # get nonce for txn input
        nonce = self.w3.eth.getTransactionCount(self.account.address)

        # get identifier for function input
        identifier = f"{name} - {unit} - {race}"

        # build transaction
        txn_dict = self.contract.functions.createRandomCharacter(
            identifier, 
            name, 
            unit, 
            race
            ).buildTransaction({
            'nonce': nonce,        
            'gas': 1648900,
            'gasPrice': self.w3.toWei('1000000000', 'wei'),
            'chainId': 3,
            })
        print("build txn dict: " + str(txn_dict))

        # sign transaction
        txn_signed = self.account.signTransaction(txn_dict)
        # print(f"Signed transaction: {txn_signed}") # Shows huge bit string

        # send transaction
        txn_hash = self.w3.eth.sendRawTransaction(txn_signed.rawTransaction)
        print(f"Transaction send with hash: {txn_hash.hex()}")

        # wait for processing
        print("waiting for nodes to handle txn")
        time.sleep(60)

        # request receipt
        txn_receipt = self.w3.eth.getTransactionReceipt(txn_hash.hex())
        print(f"Requested receipt: {txn_receipt}")

        # return creation of character
        newcharacter = f"added {name} a {unit} consist of {race}"

        return newcharacter

    def create_event(self, characterId, description):
        """create an event for a specific character by sending input to the smart contract of cryptocharacter"""
        # get nonce for txn input
        nonce = self.w3.eth.getTransactionCount(self.account.address)

        # construct transaction
        txn_dict = self.contract.functions.createEvent(
            characterId, 
            description
            ).buildTransaction({
            'nonce': nonce,        
            'gas': 1648900,
            'gasPrice': self.w3.toWei('1000000000', 'wei'),
            'chainId': 3,
            })
        # print(f"Constructed transaction: {txn_construct}") # Shows huge bit string

        # sign transaction
        txn_signed = self.account.signTransaction(txn_dict)
        # print(f"Signed transaction: {txn_signed}") # Shows huge bit string

        # send transaction
        txn_hash = self.w3.eth.sendRawTransaction(txn_signed.rawTransaction)
        print(f"Transaction send with hash: {txn_hash.hex()}")

        # wait for processing
        print("waiting for nodes to handle txn")
        time.sleep(60)

        # request receipt
        txn_receipt = self.w3.eth.getTransactionReceipt(txn_hash.hex())
        print(f"Requested receipt: {txn_receipt}")

        # return created event
        newevent = f"Added event for {characterId}: {description}"

        return newevent

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