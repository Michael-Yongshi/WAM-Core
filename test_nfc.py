
from lib.py_library_nfc.source.class_nfc import (
    NDEFcoding,
    NFCreference,
    NFCdecoder,
    NFCconnection,
)

from lib.py_library_nfc.source.class_conversions import (
    ConvertingNumbers,
    DecodingCharacter,
    EncodingCharacter,
)

def test_connect_any():
    connect = NFCconnection.initialize_any()

    # get some info out of ATR:
    atr_info = connect.get_atr_info()
    print(f"ATR information is: {atr_info}")

    connect.identify_card()

    response = connect.read_card() # nfc cards return an array of hexadecimals of 4 byte size (00 - FF; 0 - 255)

    return response

def test_connect_specific():

    atr = [59, 143, 128, 1, 128, 79, 12, 160, 0, 0, 3, 6, 3, 0, 3, 0, 0, 0, 0, 104]
    connect = NFCconnection.initialize_specific(atr)

    # get some info out of ATR:
    atr_info = connect.get_atr_info()
    print(f"ATR information is: {atr_info}")

    connect.identify_card()

    response = connect.read_card()

    return response

def test_decode(response):

    response_payload = 0
    message = 0
    print(message)

    return message

def ndef_test():

    response = 0
    response_payload = bytearray.fromhex("9101085402656e48656c6c6f5101085402656e576f726c64")

    message = NDEFcoding.decode_message(response_payload)
    print(f"returned message: {message}")

    return message

if __name__ == '__main__':

    response = test_connect_any()
    # response = test_connect_specific()

    message_ndef = ndef_test()