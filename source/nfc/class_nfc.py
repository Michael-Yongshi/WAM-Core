# https://pyscard.sourceforge.io/user-guide.html
# Sample script for the card centric approach
from __future__ import print_function
from smartcard.ATR import ATR
from smartcard.CardType import ATRCardType, AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes

class NFCconnection(object):
    def __init__(self, cardservice):
        super().__init__()
        self.cardservice = cardservice
       
    @staticmethod
    def initialize(atr, atrhex):

        # data for the card based on the received ATR (using nfc tools)
        mycardatr = atr
        print(f"mycardatr: {mycardatr}")
        mycardhex = toHexString(atrhex)
        print(f"mycardhex: {mycardhex}")
        mycardbytes = toBytes(mycardhex)
        print(f"mycardbytes: {mycardbytes}")

        # Sample script for the smartcard.ATR utility class.
        atr = ATR(atrhex)

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

        return NFCconnection(
            cardservice = cardservice,
        )

    def read_card(self, op_type):
    
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

        # use the following details (in tutorial DF_TELECOM)
        # op_details = [0x05, 0x00, 0x00, 0x00, 0x00, 0x00]

        # in order to log the details of the op_details variable we translate the bytes to hex so they become human readable
        # op_detailshex = []
        # for i in op_details:
        #     hexstring = hex(i)
        #     hexstring12 = hexstring[0] + hexstring[1]
        #     if len(hexstring) == 3:
        #         hexstring34 = hexstring[2].upper() + "0"
        #     else:
        #         hexstring34 = hexstring[2].upper() + hexstring[3].upper()
        #     hexstring = hexstring12 + hexstring34
        #     op_detailshex += [hexstring]

        # print(f"op_details hex: {op_detailshex}")
        # print(f"op_details: {op_details}")

        apdu = op_type # + op_details
        print(f"sending {toHexString(apdu)}")

        # response, sw1, sw2 = cardservice.connection.transmit( apdu, CardConnection.T1_protocol )
        response, sw1, sw2 = self.cardservice.connection.transmit(apdu)
        print(f"response: {response} status words: {sw1} {sw2}")

        return response