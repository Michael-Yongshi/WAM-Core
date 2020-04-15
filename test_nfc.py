
from lib.py_library_nfc.source.class_nfc import (
    NDEFcoding,
    NFCreference,
    NFCconnection,
)

from lib.py_library_nfc.source.class_conversions import (
    ConvertingNumbers,
    DecodingCharacter,
    EncodingCharacter,
)

def test_connect_any():
    connect = NFCconnection.initialize_any()

    return connect

def test_connect_specific():

    atr = [59, 143, 128, 1, 128, 79, 12, 160, 0, 0, 3, 6, 3, 0, 3, 0, 0, 0, 0, 104]
    connect = NFCconnection.initialize_specific(atr)

    # get some info out of ATR:
    atr_info = connect.get_atr_info()
    print(f"ATR information is: {atr_info}")

    connect.identify_card()

    response = connect.read_card()

    return response

def test_read(connect):

    response = connect.read_card()

    return response

if __name__ == '__main__':

    connect = test_connect_any()
    # connect = test_connect_specific()

    read = test_read(connect)