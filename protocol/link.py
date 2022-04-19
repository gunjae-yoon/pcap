from .protocol import *
from enum import *
import sys

class LinkType(Enum):
    LINKTYPE_NULL = 0
    LINKTYPE_ETHERNET = 1
    LINKTYPE_AX25 = 3
    LINKTYPE_IEEE802_5 = 6
    LINKTYPE_ARCNET_BSD = 7
    LINKTYPE_SLIP = 8
    LINKTYPE_PPP = 9
    LINKTYPE_FDDI = 10
    LINKTYPE_PPP_HDLC = 50
    LINKTYPE_PPP_ETHER = 51
    LINKTYPE_ATM_RFC1483 = 100
    LINKTYPE_RAW = 101
    LINKTYPE_C_HDLC = 104
    LINKTYPE_IEEE802_11 = 105
    LINKTYPE_FRELAY = 107
    LINKTYPE_LOOP = 108
    LINKTYPE_LINUX_SLL = 113
    LINKTYPE_LTALK = 114
    LINKTYPE_PFLOG = 117
    LINKTYPE_IEEE802_11_PRISM = 119
    LINKTYPE_IP_OVER_FC = 122
    LINKTYPE_SUNATM = 123
    LINKTYPE_IEEE802_11_RADIOTAP = 127
    LINKTYPE_ARCNET_LINUX = 129
    LINKTYPE_APPLE_IP_OVER_IEEE1394 = 138
    LINKTYPE_MTP2_WITH_PHDR = 139
    LINKTYPE_MTP2 = 140
    LINKTYPE_MTP3 = 141
    LINKTYPE_SCCP = 142
    LINKTYPE_DOCSIS = 143
    LINKTYPE_LINUX_IRDA = 144
    LINKTYPE_USER0 = 147
    LINKTYPE_USER1 = 148
    LINKTYPE_USER2 = 149
    LINKTYPE_USER3 = 150
    LINKTYPE_USER4 = 151
    LINKTYPE_USER5 = 152
    LINKTYPE_USER6 = 153
    LINKTYPE_USER7 = 154
    LINKTYPE_USER8 = 155
    LINKTYPE_USER9 = 156
    LINKTYPE_USER10 = 157
    LINKTYPE_USER11 = 158
    LINKTYPE_USER12 = 159
    LINKTYPE_USER13 = 160
    LINKTYPE_USER14 = 161
    LINKTYPE_USER15 = 162
    LINKTYPE_IEEE802_11_AVS = 163
    LINKTYPE_BACNET_MS_TP = 165
    LINKTYPE_PPP_PPPD = 166
    LINKTYPE_GPRS_LLC = 169
    LINKTYPE_GPF_T = 170
    LINKTYPE_GPF_F = 171
    LINKTYPE_LINUX_LAPD = 177
    LINKTYPE_MFR = 182
    LINKTYPE_BLUETOOTH_HCI_H5 = 187
    LINKTYPE_USB_LINUX = 189
    LINKTYPE_PPI = 192
    LINKTYPE_IEEE802_15_4_WITHHFCS = 195
    LINKTYPE_SITA = 196
    LINKTYPE_ERF = 197
    LINKTYPE_BLUETOOTH_HCI_H4_WITH_PHDR = 201
    LINKTYPE_AX25_KISS = 202
    LINKTYPE_LAPD = 203
    LINKTYPE_PPP_WITH_DIR = 204
    LINKTYPE_C_HDLC_WITH_DIR = 205
    LINKTYPE_FRELAY_WITH_DIR = 206
    LINKTYPE_LAPD_WITH_DIR = 207
    LINKTYPE_IPMB_LINUX = 209
    LINKTYPE_FLEXRAY = 210
    LINKTYPE_LIN = 212
    LINKTYPE_IEEE802_15_4_NONASK_PHY = 215
    LINKTYPE_USB_LINUX_MMAPPED = 220
    LINKTYPE_FC_2 = 224
    LINKTYPE_FC_2_WITH_FRAME_DELIMS = 225
    LINKTYPE_IPNET = 226
    LINKTYPE_CAN_SOCKETCAN = 227
    LINKTYPE_IPV4 = 228
    LINKTYPE_IPV6 = 229
    LINKTYPE_IEEE802_15_4_NOFCS = 230
    LINKTYPE_DBUS = 231
    LINKTYPE_DVB_CI = 235
    LINKTYPE_MUX27010 = 236
    LINKTYPE_STANAG_5066_D_PDU = 237
    LINKTYPE_NFLOG = 239
    LINKTYPE_NETANALYZER = 240
    LINKTYPE_NETANALYZER_TRANSPARENT = 241
    LINKTYPE_IPOIB = 242
    LINKTYPE_MPEG_2_TS = 243
    LINKTYPE_NG40 = 244
    LINKTYPE_NFC_LLCP = 245
    LINKTYPE_INFINIBAND = 247
    LINKTYPE_SCTP = 248
    LINKTYPE_USBPCAP = 249
    LINKTYPE_RTAC_SERIAL = 250
    LINKTYPE_BLUETOOTH_LE_LL = 251
    LINKTYPE_NETLINK = 253
    LINKTYPE_BLUETOOTH_LINUX_MONITOR = 254
    LINKTYPE_BLUETOOTH_BREDR_BB = 255
    LINKTYPE_BLUETOOTH_LE_LL_WITH_PHDR = 256
    LINKTYPE_PROFIBUS_DL = 257
    LINKTYPE_PKTAP = 258
    LINKTYPE_EPON = 259
    LINKTYPE_IPMI_HPM_2 = 260
    LINKTYPE_ZWAVE_R1_R2 = 261
    LINKTYPE_ZWAVE_R3 = 262
    LINKTYPE_WATTSTOPPER_DLM = 263
    LINKTYPE_ISO_14443 = 264
    LINKTYPE_RDS = 265
    LINKTYPE_USB_DARWIN = 266
    LINKTYPE_SDLC = 268
    LINKTYPE_LORATAP = 270
    LINKTYPE_VSOCK = 271
    LINKTYPE_NORDIC_BLE = 272
    LINKTYPE_DOCSIS31_XRA31 = 273
    LINKTYPE_ETHERNET_MPACKET = 274
    LINKTYPE_DISPLAYPORT_AUX = 275
    LINKTYPE_LINUX_SLL2 = 276
    LINKTYPE_OPENVIZSLA = 278
    LINKTYPE_EBHSCR = 279
    LINKTYPE_VPP_DISPATCH = 280
    LINKTYPE_DSA_TAG_BRCM = 281
    LINKTYPE_DSA_TAG_BRCM_PREPEND = 282
    LINKTYPE_IEEE802_15_4_TAP = 283
    LINKTYPE_DSA_TAG_DSA = 284
    LINKTYPE_DSA_TAG_EDSA = 285
    LINKTYPE_ELEE = 286
    LINKTYPE_Z_WAVE_SERIAL = 287
    LINKTYPE_USB_2_0 = 288
    LINKTYPE_ATCS_ALP = 289
    LINKTYPE_ETW = 290
    LINKTYPE_ZBOSS_NCP = 292

class LinkLayer(Protocol):
    class LinuxSLL(Protocol):
        # LInkLayer::LInuxSLL
        def __init__(self):
            self.protocolName = 'linux cooked capture'
            self.packetType = 0
            self.addressType = 0
            self.addressLength = 0
            self.sourceAddress = 0
            self.protocolType = 0

        # LInkLayer::LInuxSLL
        def parse(self, stream, offset=0):
            self.packetType = int.from_bytes(stream[offset:offset+2], byteorder='big')
            self.addressType = int.from_bytes(stream[offset+2:offset+4], byteorder='big')
            self.addressLength = int.from_bytes(stream[offset+4:offset+6], byteorder='big')
            self.sourceAddress = stream[offset+6:offset+14]
            self.protocolType = int.from_bytes(stream[offset+14:offset+16], byteorder='big')
            return True

        # LInkLayer::LInuxSLL
        def toString(self, indentationLevel=0):
            indentation = makeIndentation(indentationLevel)
            message = ''
            message += f'{indentation}packet type: {self.packetType},\n'
            message += f'{indentation}address type: {self.addressType},\n'
            message += f'{indentation}address length: {self.addressLength},\n'
            message += f'{indentation}source address: '
            for idx in range(self.addressLength):
                message += '%02x'%self.sourceAddress[idx]
                if idx < self.addressLength-1:
                    message += ':'
                else:
                    message += ',\n'
            message += f'{indentation}protocol type: 0x{self.protocolType:04x},\n'
            return message

        # LInkLayer::LInuxSLL
        def size(self):
            return 2 + 2 + 2 + 8 + 2

    class Ehternet(Protocol):
        class Header(Protocol):
            # LInkLayer::Ethernet::Header
            def __init__(self):
                self.protocolName = 'Ethernet Header'
                self.dstAddress = []
                self.srcAddress = []
                self.etherType = 0

            # LInkLayer::Ethernet::Header
            def parse(self, stream, offset=0):
                return True

            # LInkLayer::Ethernet::Header
            def toString(self, indentationLevel=0):
                indentation = makeIndentation(indentationLevel)
                message = ''
                return message

            # LInkLayer::Ethernet::Header
            def size(self):
                return 0

        class EhternetII(Protocol):
            # LInkLayer::Ethernet::EnternetII
            def __init__(self):
                self.protocolName = 'Ethernet II'

            # LInkLayer::Ethernet::EnternetII
            def parse(self, stream, offset=0):
                return True

            # LInkLayer::Ethernet::EnternetII
            def toString(self, indentationLevel=0):
                indentation = makeIndentation(indentationLevel)
                message = ''
                return message

            # LInkLayer::Ethernet::EnternetII
            def size(self):
                return 0

        class EhternetNovel(Protocol):
            # LInkLayer::Ethernet::EnternetNovel
            def __init__(self):
                self.protocolName = 'Novel raw IEEE 802.3'

            # LInkLayer::Ethernet::EnternetNovel
            def parse(self, stream, offset=0):
                return True

            # LInkLayer::Ethernet::EnternetNovel
            def toString(self, indentationLevel=0):
                indentation = makeIndentation(indentationLevel)
                message = ''
                return message

            # LInkLayer::Ethernet::EnternetNovel
            def size(self):
                return 0

        class EhternetLLC(Protocol):
            # LInkLayer::Ethernet::EnternetLLC
            def __init__(self):
                self.protocolName = 'IEEE 802.2 LLC'

            # LInkLayer::Ethernet::EnternetLLC
            def parse(self, stream, offset=0):
                return True

            # LInkLayer::Ethernet::EnternetLLC
            def toString(self, indentationLevel=0):
                indentation = makeIndentation(indentationLevel)
                message = ''
                return message

            # LInkLayer::Ethernet::EnternetLLC
            def size(self):
                return 0

        class EhternetSNAP(Protocol):
            # LInkLayer::Ethernet::EnternetSNAP
            def __init__(self):
                self.protocolName = 'IEEE 802.2 SNAP'

            # LInkLayer::Ethernet::EnternetSNAP
            def parse(self, stream, offset=0):
                return True

            # LInkLayer::Ethernet::EnternetSNAP
            def toString(self, indentationLevel=0):
                indentation = makeIndentation(indentationLevel)
                message = ''
                return message

            # LInkLayer::Ethernet::EnternetSNAP
            def size(self):
                return 0

        # LinkLayer::Ethernet
        def __init__(self):
            self.protocolName = 'Ethernet'

        # LinkLayer::Ethernet
        def parse(self, stream, offset=0):
            return True

        # LinkLayer::Ethernet
        def toString(self, indentationLevel=0):
            indentation = makeIndentation(indentationLevel)
            message = ''
            return message

        # LinkLayer::Ethernet
        def size(self):
            return 0

    # LinkLayer
    def __init__(self):
        self.protocolName = 'link layer'
        self.header = None
        self.content = None

    # LinkLayer
    def parse(self, stream, offset=0, linktype=0):
        try:
            linkType = LinkType(linktype)
        except:
            return False

        if linkType == LinkType.LINKTYPE_LINUX_SLL:
            self.header = LinkLayer.LinuxSLL()

        self.header.parse(stream, offset)

        offset += self.header.size()

        # TODO: parse protocol layer

        return True

    # LinkLayer
    def toString(self, indentationLevel=0):
        indentation = makeIndentation(indentationLevel)
        message = ''
        message += f'{indentation}{self.header}\n'
        message += f'{indentation}header: {{\n'
        message += f'{self.header.toString(indentationLevel+1)}'
        message += f'{indentation}}},\n'
        message += f'{indentation}content: {{\n'
        #message += f'{self.content.toString(indentationLevel+1)}'
        message += f'{indentation}}}\n'
        return message

    # LinkLayer
    def size(self):
        return 0

