#!/usr/bin/python
import getopt
import sys


from GXByteBuffer import GXByteBuffer
from GXDLMSChipperingStream import GXDLMSChipperingStream


def main(argv):
    key = ""
    system_title = ""
    security_byte = ""
    frame_counter = ""
    encrypted = ""

    help_text = 'rch_simple.py -k <key> -t <system title> -b <securityByte> -f <frameCounter> -d <encryptedData>'

    try:
        opts, args = getopt.getopt(
            argv,
            "hk:t:b:f:d:",
            ["key", "systemTitle", "securityByte", "frameCounter", "encryptedData"]
        )
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-k", "--key"):
            key = arg
        elif opt in ("-t", "--systemTitle"):
            system_title = arg
        elif opt in ("-b", "--securityByte"):
            security_byte = arg
        elif opt in ("-f", "--frameCounter"):
            frame_counter = arg
        elif opt in ("-d", "--encryptedData"):
            encrypted = arg

    # decrypt own
    security = int(security_byte, 16)
    tag = bytearray(12)
    iv = GXByteBuffer.hexToBytes(system_title + frame_counter)
    aad = key = GXByteBuffer.hexToBytes(key)

    gcm = GXDLMSChipperingStream(security, True, key, aad, iv, tag)
    gcm.write(GXByteBuffer.hexToBytes(encrypted))
    print(''.join(format(x, '02x') for x in gcm.flushFinalBlock()))


if __name__ == "__main__":
    main(sys.argv[1:])
