from wakeonlan import send_magic_packet
from macs import *


def wakePDV():
    for key in macs:
        print("Ligando:", key)
        send_magic_packet(macs[key])
        
wakePDV()