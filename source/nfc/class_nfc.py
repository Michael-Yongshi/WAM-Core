import os
import time

from web3 import Web3

from source.methods_json import load_json

class NFCconnection(object):
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
