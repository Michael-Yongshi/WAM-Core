# https://pyscard.sourceforge.io/user-guide.html
# Sample script for the card centric approach
from __future__ import print_function
from smartcard.ATR import ATR
from smartcard.CardType import ATRCardType
from smartcard.CardRequest import CardRequest
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

cardtype = ATRCardType(mycardbytes)
cardrequest = CardRequest( timeout=1, cardType=cardtype )

print("Waiting for card")
cardservice = cardrequest.waitforcard()
print("Card connected")

cardservice.connection.connect()
print("connected to reader: " + str(cardservice.connection.getReader()))
print("connected to card: " + str(toHexString(cardservice.connection.getATR())))

# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
# data, sw1, sw2 = cardservice.connection.transmit( SELECT + DF_TELECOM )
# print(sw1, sw2)