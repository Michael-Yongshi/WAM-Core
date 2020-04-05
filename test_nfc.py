
from lib.python_nfc_lib.class_nfc import (
    NFCreference,
    NDEFinterpreter,
    NFCconnection,
)

from lib.python_nfc_lib.class_conversions import (
    ConvertingNumbers,
    DecodingCharacter,
    EncodingCharacter,
)

def test_formatting():
    startbytes = [85, 203, 230, 191]
    print(f"Converting {startbytes} to hex and back to bytes")
    bytes_to_hex = NFCmethods.bytes_to_hex(startbytes)
    print(f"bytes to hex: {bytes_to_hex}")
    hex_to_bytes = NFCmethods.hex_to_bytes(bytes_to_hex)
    print(f"hex to bytes: {hex_to_bytes}")
    print("")

    starthex = [0xBF, 0xE6, 0xCB, 0x55]
    starthexliteral = "[0xBF, 0xE6, 0xCB, 0x55]"
    print(f"Converting {starthexliteral} to bytes and back to hex")
    hex_to_bytes = NFCmethods.hex_to_bytes(starthex)
    print(f"hex to bytes: {hex_to_bytes}")
    bytes_to_hex = NFCmethods.bytes_to_hex(hex_to_bytes)
    print(f"bytes to hex: {bytes_to_hex}")
    print("")

if __name__ == '__main__':

    test_connect_any = NFCconnection.initialize_any()
    print("")
    test_connect_any.get_card_uid()
    print("")
    response = test_connect_any.get_card_data() # nfc cards return an array of hexadecimals of 4 byte size (00 - FF; 0 - 255)
    print("")
    message = NDEFinterpreter.decode_message(response)

    uid = [52, 3, 120, 210, 10, 107, 116, 101]
    uidhex = []
    for i in uid:
        uidhex += [ConvertingNumbers.int_to_hex(i)]
    
    print(f"uid = {uid}, uidhex = {uidhex}")
