import nfc
import ndef
from threading import Thread

import libusb1

import serial


# def beam(llc):
#     snep_client = nfc.snep.SnepClient(llc)
#     snep_client.put_records([ndef.UriRecord('http://nfcpy.org')])

# def connected(llc):
#     Thread(target=beam, args=(llc,)).start()
#     return True

with nfc.ContactlessFrontend() as clf:
    assert clf.open('usb:002:009') is True
    device = clf.open('usb')
    print(device)
    device = clf.open('usb:002:009')
    print(device)