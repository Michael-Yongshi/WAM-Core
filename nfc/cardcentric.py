# https://pyscard.sourceforge.io/user-guide.html
# Sample script for the card centric approach
from __future__ import print_function
from smartcard.ATR import ATR
from smartcard.CardType import ATRCardType, AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes


# data for the card based on the received ATR (using nfc tools)
mycardatr = "3B:8F:80:01:80:4F:0C:A0:00:00:03:06:03:00:01:00:00:00:00:6A"
mycardstring = "3B 8F 80 01 80 4F 0C A0 00 00 03 06 03 00 01 00 00 00 00 6A"
mycardbytes = toBytes(mycardstring)
mycardhex = [0x3B, 0x8F, 0x80, 0x01, 0x80, 0x4F, 0x0C, 0xA0, 0x00, 0x00, 0x03, 0x06, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x6A]


# Sample script for the smartcard.ATR utility class.
atr = ATR(mycardhex)

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

# Select determines what kind of card to be selected???
# MF card?
select = [
    0x00, # CLS ?
    0xA4, # INS ?
    0x00, # P1 field?
    0x00, # P2 field?
    0x02, # Number of bytes to read
    0x3F, # File id part 1
    0x01, # file id part 2
    ]

# read data
read = [
    0x00,
    0xB0,
    0x00,
    0x00,
    0x05,
]

# write data
write = [
    0x00,
    0xD0,
    0x00,
    0x00,
    0x05,
]

# in order to log the details of the select variable we translate the bytes to hex so they become human readable
selecthex = []
for i in select:
    hexstring = hex(i)
    hexstring12 = hexstring[0] + hexstring[1]
    if len(hexstring) == 3:
        hexstring34 = hexstring[2].upper() + "0"
    else:
        hexstring34 = hexstring[2].upper() + hexstring[3].upper()
    hexstring = hexstring12 + hexstring34
    selecthex += [hexstring]

print(f"select hex: {selecthex}")
print(f"select: {select}")

df_telecom = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
df_telecomhex = []
for i in df_telecom:
    df_telecomhex += [hex(i)]
print(f"df_telecom hex: {df_telecomhex}")
print(f"df_telecom: {df_telecom}")

apdu = select + df_telecom
print(f"sending {toHexString(apdu)}")

# response, sw1, sw2 = cardservice.connection.transmit( apdu, CardConnection.T1_protocol )
response, sw1, sw2 = cardservice.connection.transmit( apdu )
print(f"response: {response} status words: {sw1} {sw2}")

# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# df_telecom = [0x7F, 0x10]
# data, sw1, sw2 = cardservice.connection.transmit( SELECT + df_telecom )
# print(sw1, sw2)