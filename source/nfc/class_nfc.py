# https://pyscard.sourceforge.io/user-guide.html
# Sample script for the card centric approach
from __future__ import print_function
from smartcard.ATR import ATR
from smartcard.CardType import ATRCardType, AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes
from smartcard.System import readers

class NFCmethods(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_handshake():
        #ACS ACR122U NFC Reader
        #Suprisingly, to get data from the tag, it is a handshake protocol
        #You send it a command to get data back
        #This command below is based on the "API Driver Manual of ACR122U NFC Contactless Smart Card Reader"
        
        handshake = [0xFF, 0xCA, 0x00, 0x00, 0x00] #handshake cmd needed to initiate data transfer
        return handshake

    @staticmethod
    def get_application_method(atrhex):
        # also known as RID or Registered App Provider Identifier
        application_method = "Unknown"

        application_methods = {
            "A000000306": "PC/SC Workgroup"
        }

        # 9th position, pythons first position is 0, so 9-1=8
        application_method_string = ""
        for i in range(7, 12):
            atri = format(atrhex[i], '#04x')[2:]
            atri = atri.upper()
            if len(atri) == 1:
                atri = "0" + atri
            application_method_string += atri

        # print(f"application_method_string: {application_method_string}")

        for key in application_methods:
            if key == application_method_string:
                application_method = application_methods[key]
                break
        
        if application_method == "Unknown":
            application_method += f" - RID code: {application_method_string}"

        return application_method

    @staticmethod
    def get_card_type(atrhex):

        card_type = "Unknown"

        card_types = {
            "0001": "Mifare 1K",
            "0002": "Mifare 4k",
            "0003": "Mifare Ultralight",
            "0026": "Mifare Mini",
            "F004": "Topaz and Jewel",
            "F011": "Felica 212k",
            "F012": "Felica 424k",
        }

        # 14th position, pythons first position is 0, so 14-1=13
        card_type_string = ""
        for i in range(13, 15):
            atri = format(atrhex[i], '#04x')[2:]
            atri = atri.upper()
            if len(atri) == 1:
                atri = "0" + atri
            card_type_string += atri

        for key in card_types:
            if key == card_type_string:
                card_type = card_types[key]
                break
        
        if card_type == "Unknown":
            card_type += f" - card name code: {card_type_string}"

        return card_type

    @staticmethod
    def stringParser(data_in):
        """--------------String Parser--------------"""
        # #([85, 203, 230, 191], 144, 0) -> [85, 203, 230, 191]
        # if isinstance(data_in, tuple):
        #     temp = data_in[0]
        #     code = data_in[1]
        # #[85, 203, 230, 191] -> [85, 203, 230, 191]
        # else:
        #     temp = data_in
        #     code = 0

        temp = data_in

        # print(f"data_in = {data_in}")
        data_out = ""

        #[85, 203, 230, 191] -> bfe6cb55 (int to hex reversed)
        for val in reversed(temp): # 85
            # print(f"val = {val}")
            formatval = format(val, '#04x')[2:] # bf
            # print(f"formatted = {formatval}")
            data_out += formatval # bfe6cb55
            # print(f"data_out = {data_out}")

        data_out = data_out.upper() #bfe6cb55 -> BFE6CB55
        # print(f"data_out_upper = {data_out}")

        return data_out

class NFCconnection(object):
    def __init__(self, cardservice):
        super().__init__()
        self.cardservice = cardservice

    @staticmethod
    def initialize_any():

        cardtype = AnyCardType() # for accepting any type of card
        cardrequest = CardRequest( timeout=1, cardType=cardtype )

        print("Waiting for card")
        cardservice = cardrequest.waitforcard()
        print("Card connected")

        # connecting to card
        cardservice.connection.connect()

        reader = cardservice.connection.getReader()
        print(f"connected to reader: {reader}")
        atr = cardservice.connection.getATR()
        print(f"connected to card (in bytes): {str(atr)}")
        atrhex = toHexString(atr)
        print(f"connected to card (in hex): {str(atrhex)}")

        # get some info out of ATR:
        rid = NFCmethods.get_application_method(atr)
        print(f"application method RID: {rid}")
        card_type = NFCmethods.get_card_type(atr)
        print(f"cardtype: {card_type}")

        response, sw1, sw2 = cardservice.connection.transmit(NFCmethods.get_handshake())
        print(f"response: {response} status words: {sw1} {sw2}")
        if sw1 == 144:
            print(f"Handshake with card succesfull!")
        else:
            print(f"Handshake failed!")

        return NFCconnection(
            cardservice = cardservice,
        )

    @staticmethod
    def initialize_specific(atr, atrhex):

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

        cardtype = AnyCardType() # for accepting any type of card
        # cardtype = ATRCardType(mycardbytes) # for accepting a specific type of card
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

    def read_card(self):
        
        data = ""
        page = 1
        while page > 0 and page < 10:
            try:
                readdata = self.read_page(page)
                print(f"retrieving page {page} resulted in {readdata}")
                data += readdata
                page += 1
            except:
                page = 0

        print(f"data of whole card is: {data}")
        return data

    def read_page(self, page):

        # Establish handshake with card
        response, sw1, sw2 = self.cardservice.connection.transmit(NFCmethods.get_handshake())
        readdata = NFCmethods.stringParser(response)
        # print(f"response: {response}, parsed: {readdata}, status words: {sw1} {sw2}")
        # if sw1 == 144:
            # print(f"Handshake with card succesfull!")
        # else:
            # print(f"Handshake failed!")

        #Read command [FF, B0, 00, page, #bytes]
        print(f"trying to retrieve page {page}")
        response, sw1, sw2 = self.cardservice.connection.transmit([0xFF, 0xB0, 0x00, page, 0x04])
        print(f"response: {response} status words: {sw1} {sw2}")

        readdata = NFCmethods.stringParser(response)

        return readdata

    def read_card_depreciated(self, op_type):
    
        ISOAPDU=  {
            'ERASE BINARY':'0E',
            'VERIFY':'20',
            # Global Platform
            'INITIALIZE_UPDATE':'50',
            # GP end
                    'MANAGE_CHANNEL':'70',
                    'EXTERNAL_AUTHENTICATE':'82',
                    'GET_CHALLENGE':'84',
                    'INTERNAL_AUTHENTICATE':'88',
                    'SELECT_FILE':'A4',
                    #vonjeek start
                    'VONJEEK_SELECT_FILE':'A5',
                    'VONJEEK_UPDATE_BINARY':'A6',
                    'VONJEEK_SET_MRZ':'A7',
            'VONJEEK_SET_BAC':'A8',
            'VONJEEK_SET_DATASET':'AA',
                    #vonjeek end
            # special for JCOP
            'MIFARE_ACCESS':'AA',
            'ATR_HIST':'AB',
            'SET_RANDOM_UID':'AC',
            # JCOP end
                    'READ_BINARY':'B0',
                    'READ_RECORD(S)':'B2',
                    'GET_RESPONSE':'C0',
                    'ENVELOPE':'C2',
                    'GET_DATA':'CA',
                    'WRITE_BINARY':'D0',
                    'WRITE_RECORD':'D2',
                    'UPDATE_BINARY':'D6',
                    'PUT_DATA':'DA',
                    'UPDATE_DATA':'DC',
            'CREATE_FILE':'E0',
                    'APPEND_RECORD':'E2',
            # Global Platform
            'GET_STATUS':'F2',
            # GP end
            'READ_BALANCE':'4C',
            'INIT_LOAD': '40',
            'LOAD_CMD':'42',
            'WRITE_MEMORY':'7A',
            'READ_MEMORY':'78',
            }

        # COMMAND : [Class, Ins, P1, P2, DATA, LEN]
        PCSC_APDU= {
            'ACS_14443_A' : ['d4','40','01'],
            'ACS_14443_B' : ['d4','42','02'],
            'ACS_14443_0' : ['d5','86','80', '05'],
            'ACS_DISABLE_AUTO_POLL' : ['ff','00','51','3f','00'],
            'ACS_DIRECT_TRANSMIT' : ['ff','00','00','00'],
            'ACS_GET_SAM_SERIAL' : ['80','14','00','00','08'],
            'ACS_GET_SAM_ID' : ['80','14','04','00','06'],
            'ACS_GET_READER_FIRMWARE' : ['ff','00','48','00','00'],
            'ACS_GET_RESPONSE' : ['ff','c0','00','00'],
            'ACS_GET_STATUS' : ['d4','04'],
            'ACS_IN_LIST_PASSIVE_TARGET' : ['d4','4a'],
            'ACS_LED_GREEN' : ['ff','00','40','0e','04','00','00','00','00'],
            'ACS_LED_ORANGE' : ['ff','00','40','0f','04','00','00','00','00'],
            'ACS_LED_RED' : ['ff','00','40','0d','04','00','00','00','00'],
            'ACS_MIFARE_LOGIN' : ['d4','40','01'],
            'ACS_READ_MIFARE' : ['d4','40','01','30'],
            'ACS_POLL_MIFARE' : ['d4','4a','01','00'],
            'ACS_POWER_OFF' : ['d4','32','01','00'],
            'ACS_POWER_ON' : ['d4','32','01','01'],
            'ACS_RATS_14443_4_OFF' : ['d4','12','24'],
            'ACS_RATS_14443_4_ON' : ['d4','12','34'],
            'ACS_SET_PARAMETERS' : ['d4','12'],
            'ACS_SET_RETRY' : ['d4','32','05','00','00','00'],
            'AUTHENTICATE' : ['ff', ISOAPDU['INTERNAL_AUTHENTICATE']],
            'GUID' : ['ff', ISOAPDU['GET_DATA'], '00', '00', '00'],
            'ACS_GET_ATS' : ['ff', ISOAPDU['GET_DATA'], '01', '00', '00'],
            'LOAD_KEY' : ['ff',  ISOAPDU['EXTERNAL_AUTHENTICATE']],
            'READ_BLOCK' : ['ff', ISOAPDU['READ_BINARY']],
            'UPDATE_BLOCK' : ['ff', ISOAPDU['UPDATE_BINARY']],
            'VERIFY' : ['ff', ISOAPDU['VERIFY']],
            'WRITE_BLOCK' : ['ff', ISOAPDU['WRITE_BINARY']],
            }

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