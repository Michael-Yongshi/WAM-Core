from ndef import (
    message_decoder,
    message_encoder,
    TextRecord,
)

from smartcard.util import toHexString, toBytes

from lib.python_nfc_lib.class_nfc import (
    NFCmethods,
    NDEFinterpreter,
    NFCconnection,
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

    NFCmethods.set_apdu_table()

    # test_formatting()

    test_connect_any = NFCconnection.initialize_any()
    print("")
    test_connect_any.get_card_uid()
    print("")
    response = test_connect_any.get_card_data(4)
    print("")
    message = NDEFinterpreter.decode_message(response)


    # data = test_connect_any.get_card_data()














    # atr = "3B:8F:80:01:80:4F:0C:A0:00:00:03:06:03:00:01:00:00:00:00:6A"
    # atrhex = [0x3B, 0x8F, 0x80, 0x01, 0x80, 0x4F, 0x0C, 0xA0, 0x00, 0x00, 0x03, 0x06, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x6A]
    
    # # operations
    # # op_type determines what kind of card to be selected???
    # # MF card?
    # # op_type = [
    # #     0x00, # CLS ? PC/SC READER COMMAND
    # #     0xA4, # INS ? instruction / operation like read (B0) or write (D0)
    # #     0x00, # P1 field?
    # #     0x00, # P2 field? block number to read / write
    # #     0x02, # Number of bytes to read
    # #     0x3F, # File id part 1
    # #     0x01, # file id part 2
    # #     ]
    # # op_type = [0xFF, 0xCA, 0x00, 0x00, 0x04] # get uid of card
    # op_type = [0xFF, 0xB0, 0x00, 0x09, 0x10] # should read: second is read operation (B0), fourth is block number 1, fifth is bytes to read 16 (two times 8 bit which is 10 in bytecode)
    # # op_type = [0xFF, 0xD0, 0x00, 0x00] # should write: second is write operation (D0), fourth is block number 1, fifth is bytes to read 16 (two times 8 bit which is 10 in bytecode)
    # # op_type = [0xFF,0x00,0x40,0x00,0x04,0x01,0x00,0x03,0x03] # beep reader

    # nfc_connect = NFCconnection.initialize_specific(atr, atrhex)
    
    # # inhex = '9101085402656e48656c6c6f5101085402656e576f726c64'
    # # octets = bytearray.fromhex(inhex)

    # inbytes = nfc_connect.read_card(op_type)