import time

from web3 import Web3

from source.methods_json import load_file

w3 = Web3(Web3.HTTPProvider("https://api.infura.io/v1/jsonrpc/ropsten"))

# the needed abi functions for this contract
abi = load_file("cryptocharacter/contracts/", "cryptocharacter_abi")

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
        'chainId': 3, 
        })

signed_txn = account.signTransaction(txn_dict)
txn_hash = contract.constructor()
txn_receipt = w3.eth.waitForTransactionReceipt(signed_txn.rawTransaction)

# Create contract instance based on the deployed smart contract
contract = w3.eth.contract(address = txn_receipt.contract_address, abi = abi)
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
txn_receipt = w3.eth.getTransactionReceipt(txn_hash.hex())


if __name__ == "__main__":
    
deploy_contract(wallet_address, wallet_private_key)
