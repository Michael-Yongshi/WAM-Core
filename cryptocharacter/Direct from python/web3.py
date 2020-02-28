import time

from web3 import Web3, HTTPProvider
from solc import compile_files


# set up w3 details
contract_address     = "0x20589989d97b41ea6b9F748CEB4a17527CaA2C1a"                           # [YOUR CONTRACT ADDRESS]
wallet_private_key   = "ad5bb5684dbfb337040fb31d76c7b6118e0bb4fed23e940451a43746f93ebb09"     # [YOUR TEST WALLET PRIVATE KEY]
wallet_address       = "0x980df35116009EB3937B0fD7931E3620114fDb9b"                           # [YOUR WALLET ADDRESS]

w3 = Web3(HTTPProvider("http://51.105.171.12")) # [YOUR NODE URL]

w3.eth.enable_unaudited_features()


# send an example transaction of ether
def send_ether_to_contract(amount_in_ether):

    amount_in_wei = w3.toWei(amount_in_ether,'ether')

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = {
            'to': contract_address,
            'value': amount_in_wei,
            'gas': 2000000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
            'chainId': 3
    }

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):

        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)

        print(txn_receipt)

        time.sleep(10)


    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

if __name__ == "__main__":
    send_ether_to_contract(1)