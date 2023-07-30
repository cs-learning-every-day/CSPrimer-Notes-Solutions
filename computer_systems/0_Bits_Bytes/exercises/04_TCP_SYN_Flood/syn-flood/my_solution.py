"""
Header:
    - Magic Number (4 Bytes)
    - Minor Version Number (2 Bytes)
    - Minor Version Number (2 Bytes)
    - Time Zone Offset (4 Bytes) - always zero
    - Accuracy of time stamps (4 Bytes) - always zero
    - Snapshot length (4 Bytes) - i.e. truncation threshold
    - Link-Layer header type (4 Bytes) - see pcap-linktype


Following this are zero or more packets

Packet Headers:
    - Time stamp of packet capture (4 bytes)
    - Time since capture in micro or nano seconds (4 bytes)
    - Number of bytes of captured data that follow the per-packet header (4 bytes)
    - Number of bytes that would have been captured without truncation (4 bytes)

All fields in byte order of the host writing the file (little endian)
"""

import enum
from dataclasses import dataclass
FILE = 'synflood.pcap'
PCAP_HEADER_OFFSET = 24
PACKET_HEADER_LENGTH = 16


class ByteOrder(str, enum.Enum):
    little = "little"
    big = 'big'


@dataclass
class PCAPHeader:
    raw: bytes
    magic_number: int
    major_version: int
    minor_version: int
    time_zone_offset: int
    time_step_accuracy: int
    snapshot_length: int
    link_layer_header_type: int
    byte_order: ByteOrder

    def __post_init__(self):
        assert self.major_version == 2
        assert self.minor_version == 4
        assert self.time_zone_offset == 0
        assert self.time_step_accuracy == 0

    @classmethod
    def build(cls, data: bytes) -> "PCAPHeader":
        return cls(
            raw=data[:PCAP_HEADER_OFFSET],
            magic_number=b2int(data[:4], ByteOrder.little),
            major_version=b2int(data[4:6], ByteOrder.little),
            minor_version=b2int(data[6:8], ByteOrder.little),
            time_zone_offset=b2int(data[8:12], ByteOrder.little),
            time_step_accuracy=b2int(data[12:16], ByteOrder.little),
            snapshot_length=b2int(data[16:20], ByteOrder.little),
            link_layer_header_type=b2int(data[20:24], ByteOrder.little),
            byte_order=ByteOrder.little
        )


def b2int(val: bytes, byte_order: ByteOrder = ByteOrder.little) -> int:
    return int.from_bytes(val, byteorder=byte_order)


@dataclass
class PCAPPacketHeader:
    raw: bytes
    capture_time_stamp: int
    time_since_capture: int
    n_bytes_captured: int
    n_bytes_captured_wo_truncation: int

    def __post_init__(self):
        assert self.n_bytes_captured == self.n_bytes_captured_wo_truncation
        assert len(self.raw) == PACKET_HEADER_LENGTH

    @classmethod
    def build(cls, data: bytes) -> "PCAPPacketHeader":
        return cls(
            raw=data,
            capture_time_stamp=b2int(data[:4]),
            time_since_capture=b2int(data[4:8]),
            n_bytes_captured=b2int(data[8:12]),
            n_bytes_captured_wo_truncation=b2int(data[12:16])
        )


@dataclass
class PacketPayload:
    raw: bytes


@dataclass
class LinkLayerHeader:
    pass


@dataclass
class IPHeader:
    pass


@dataclass
class TCPHeader:
    pass


@dataclass
class Packet:
    pcap_header: PCAPPacketHeader
    link_layer_header: LinkLayerHeader # 4 bytes
    ip_header: IPHeader
    tcp_header: TCPHeader
    payload: PacketPayload

    @property
    def raw(self) -> bytes:
        return self.header.raw + self.payload.raw


def main():
    with open(FILE, 'rb') as f:
        data = f.read()

    header = PCAPHeader.build(data)
    PAYLOAD_1_OFFSET = PCAP_HEADER_OFFSET + PACKET_HEADER_LENGTH
    packet_1 = PCAPPacketHeader.build(
        data[PCAP_HEADER_OFFSET:PAYLOAD_1_OFFSET]
    )
    payload_1 = PacketPayload(raw=data[PAYLOAD_1_OFFSET:PAYLOAD_1_OFFSET+packet_1.n_bytes_captured])
    print(payload_1)


if __name__ == '__main__':
    main()

