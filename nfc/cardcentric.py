# https://pyscard.sourceforge.io/user-guide.html
# Sample script for the card centric approach
from __future__ import print_function
from smartcard.ATR import ATR
from smartcard.CardType import ATRCardType, AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes


def get_card(atr, atrlistbytes):
    # data for the card based on the received ATR (using nfc tools)
    mycardatr = atr
    print(f"mycardatr: {mycardatr}")
    mycardhex = toHexString(atrhex)
    print(f"mycardhex: {mycardhex}")
    mycardbytes = toBytes(mycardhex)
    print(f"mycardbytes: {mycardbytes}")

    # Sample script for the smartcard.ATR utility class.
    atr = ATR(atrlistbytes)

    print(atr)
    print('historical bytes: ', toHexString(atr.getHistoricalBytes()))
    print('checksum: ', "0x%X" % atr.getChecksum())
    print('checksum OK: ', atr.checksumOK)
    print('T0  supported: ', atr.isT0Supported())
    print('T1  supported: ', atr.isT1Supported())
    print('T15 supported: ', atr.isT15Supported())

    # cardtype = AnyCardType() # for accepting any type of card
    cardtype = ATRCardType(mycardbytes)
    cardrequest = CardRequest( timeout=1, cardType=cardtype )

    print("Waiting for card")
    cardservice = cardrequest.waitforcard()
    print("Card connected")

    # connecting to card
    cardservice.connection.connect()
    # cardservice.connection.connect( CardConnection.T1_protocol) # Connecting with a specific T1 or T2 protocol

    print("connected to reader: " + str(cardservice.connection.getReader()))
    print("connected to card (in bytes): " + str(cardservice.connection.getATR()))
    print("connected to card (in hex): " + str(toHexString(cardservice.connection.getATR())))
    print("this is my card") if cardservice.connection.getATR() == mycardbytes else print("this is not my card")

    return cardservice

def read_card(atr, atrlistbytes):
    
    cardservice = get_card(atr, atrlistbytes)

    # op_type determines what kind of card to be selected???
    # MF card?
    # op_type = [
    #     0x00, # CLS ?
    #     0xA4, # INS ?
    #     0x00, # P1 field?
    #     0x00, # P2 field?
    #     0x02, # Number of bytes to read
    #     0x3F, # File id part 1
    #     0x01, # file id part 2
    #     ]

    # valid, but dont know what it does
    # op_type = [
    #     0xFF,
    #     0x82,
    #     0x00,
    #     0x00,
    #     0x05,
    # ]

    # should result in getting uid of card but response is empty
    op_type = [
        0xFF, 
        0xCA, 
        0x00, 
        0x00,
        0x00,
        ]

    # read data
    # op_type = [
    #     0x00,
    #     0xB0,
    #     0x00,
    #     0x00,
    # ]

    # # write data
    # op_type = [
    #     0x00,
    #     0xD0,
    #     0x00,
    #     0x00,
    # ]

    # in order to log the details of the op_type variable we translate the bytes to hex so they become human readable
    op_typehex = []
    for i in op_type:
        hexstring = hex(i)
        hexstring12 = hexstring[0] + hexstring[1]
        if len(hexstring) == 3:
            hexstring34 = hexstring[2].upper() + "0"
        else:
            hexstring34 = hexstring[2].upper() + hexstring[3].upper()
        hexstring = hexstring12 + hexstring34
        op_typehex += [hexstring]

    print(f"op_type hex: {op_typehex}")
    print(f"op_type: {op_type}")

    op_details = [0x05, 0x00, 0x00, 0x00, 0x00, 0x00]

    # in order to log the details of the op_details variable we translate the bytes to hex so they become human readable
    op_detailshex = []
    for i in op_details:
        hexstring = hex(i)
        hexstring12 = hexstring[0] + hexstring[1]
        if len(hexstring) == 3:
            hexstring34 = hexstring[2].upper() + "0"
        else:
            hexstring34 = hexstring[2].upper() + hexstring[3].upper()
        hexstring = hexstring12 + hexstring34
        op_detailshex += [hexstring]

    print(f"op_details hex: {op_detailshex}")
    print(f"op_details: {op_details}")

    apdu = op_type + op_details
    print(f"sending {toHexString(apdu)}")

    # response, sw1, sw2 = cardservice.connection.transmit( apdu, CardConnection.T1_protocol )
    response, sw1, sw2 = cardservice.connection.transmit( apdu )
    print(f"response: {response} status words: {sw1} {sw2}")



if __name__ == '__main__':
    atr = "3B:8F:80:01:80:4F:0C:A0:00:00:03:06:03:00:01:00:00:00:00:6A"
    atrhex = [0x3B, 0x8F, 0x80, 0x01, 0x80, 0x4F, 0x0C, 0xA0, 0x00, 0x00, 0x03, 0x06, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x6A]
    
    get_card(atr, atrhex)
    read_card(atr, atrhex)