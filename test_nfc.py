
from lib.wam_library_nfc.source.class_nfc import (
    NFCreference,
    NDEFinterpreter,
    NFCconnection,
)

from lib.wam_library_nfc.source.class_conversions import (
    ConvertingNumbers,
    DecodingCharacter,
    EncodingCharacter,
)


if __name__ == '__main__':

    # test connection
    test_connect_any = NFCconnection.initialize_any()
    print("")

    # test connection
    # test_connect_any = NFCconnection.initialize_specific([59, 143, 128, 1, 128, 79, 12, 160, 0, 0, 3, 6, 3, 0, 3, 0, 0, 0, 0, 104])
    # print("")

    # get some info out of ATR:
    atr_info = test_connect_any.get_atr_info()
    print(f"ATR information is: {atr_info}")
    print("")

    # test_connect_any.identify_card()
    # print("")

    # response = test_connect_any.read_card() # nfc cards return an array of hexadecimals of 4 byte size (00 - FF; 0 - 255)
    # print("")

    # message = NDEFinterpreter.decode_message(response)

    # uid = [52, 3, 120, 210, 10, 107, 116, 101]
    # uidhex = []
    # for i in uid:
    #     uidhex += [ConvertingNumbers.int_to_hex(i)]
    
    # print(f"uid = {uid}, uidhex = {uidhex}")
