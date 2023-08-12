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
from typing import Optional
from tqdm import tqdm
from dataclasses import dataclass
FILE = 'synflood.pcap'
PCAP_HEADER_OFFSET = 24
PACKET_HEADER_LENGTH = 16


class ByteOrder(str, enum.Enum):
    little = "little"
    big = 'big'


class LinkLayerHeaderType(enum.Enum):
    NULL = 0


@dataclass
class PCAPHeader:
    raw: bytes
    magic_number: int
    major_version: int
    minor_version: int
    time_zone_offset: int
    time_step_accuracy: int
    snapshot_length: int
    link_layer_header_type: LinkLayerHeaderType
    byte_order: ByteOrder

    def __post_init__(self):
        assert self.magic_number == 0xa1b2c3d4
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
            link_layer_header_type=LinkLayerHeaderType(
                b2int(data[20:24], ByteOrder.little)
            ),
            byte_order=ByteOrder.little
        )


def b2int(val: bytes, byte_order: ByteOrder = ByteOrder.little) -> int:
    return int.from_bytes(val, byteorder=byte_order)  # type: ignore


def le2int(val: bytes) -> int:
    return b2int(val, ByteOrder.little)


def be2int(val: bytes) -> int:
    return b2int(val, ByteOrder.big)


@dataclass
class PacketHeader:
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
class IPHeader:
    raw: bytes
    version: int #4 bits
    IHL: int # 4 bits
    DSCP: int #6 bits
    ECN: int # 2 bits
    total_length: int #16 bits (1 Byte)
    identification: int # 16 bits (1 Byte)
    flags: int # 3 bits
    fragment_offset: int # 13 bits
    time_to_live: int # 8 bits (1 Byte)
    protocol: int # 8 bits (1 Byte)
    header_checksum: int # 16 bits (2 bytes)
    source_ip_address: int # 32 bits (4 bytes)
    destination_ip_address: int # 32 bits (4 bytes)

    def __post_init__(self):
        assert self.version == 4
        assert len(self.raw) == self.total_length

    @classmethod
    def build(cls, data: bytes) -> "IPHeader":
        version = data[0] >> 4
        IHL = (data[0] & 0b1111 ) # gets # of rows of IP Header
        #IHL <= 2 # Converts IHL to number of bytes (4 bytes per row)
        DSCP = data[1] >> 2
        ECN = data[1] & 0b11
        total_length = be2int(data[2:4])
        identification = be2int(data[4:6])
        flags = data[7] >> 5
        fragment_offset = data[7] & 0b1111111111111
        time_to_live = data[8]
        protocol = data[9]
        header_checksum = be2int(data[10:12])
        source_ip_address = be2int(data[12:16])
        destination_ip_address = be2int(data[16:20])
        return cls(
            raw=data,
            version=version,
            IHL=IHL,
            DSCP=DSCP,
            ECN=ECN,
            total_length=total_length,
            identification=identification,
            flags=flags,
            fragment_offset=fragment_offset,
            time_to_live=time_to_live,
            protocol=protocol,
            header_checksum=header_checksum,
            source_ip_address=source_ip_address,
            destination_ip_address=destination_ip_address,
        )


@dataclass
class TCPHeader:
    raw: bytes
    source_port: int # 2 bytes
    destination_port: int # 2 bytes
    sequence_number: int # 4 bytes
    ack_number: int # 4 bytes
    data_offset: int # 4 bits
    CWR: int # 1 bit
    ECE: int # 1 bit
    URG: int # 1 bit
    ACK: int # 1 bit
    PSH: int # 1 bit
    RST: int # 1 bit
    SYN: int # 1 bit
    FIN: int # 1 bit
    window_size: int # 1 byte
    checksum: int # 2 bytes
    urgent_pointer: int # 2 bytes
    options: bytes


    @classmethod
    def build(cls, data: bytes) -> "TCPHeader":
        source_port = be2int(data[0:2])
        destination_port = be2int(data[2:4])
        sequence_number = be2int(data[4:8])
        ack_number = be2int(data[8:12])
        data_offset = data[12] >> 4
        CWR = data[13] >> 7
        ECE = (data[13] & 0b1111111) >> 6
        URG = (data[13] & 0b111111) >> 5
        ACK = (data[13] & 0b11111) >> 4
        PSH = (data[13] & 0b1111) >> 3
        RST = (data[13] & 0b111) >> 2
        SYN = (data[13] & 0b11) >> 1
        SYN = (data[13] & 0x0002)
        FIN = data[13] & 0b1
        window_size = be2int(data[14:16])
        checksum = be2int(data[16:18])
        urgent_pointer = be2int(data[18:20])
        options = data[20:]

        return cls(
            raw=data,
            source_port=source_port,
            destination_port=destination_port,
            sequence_number=sequence_number,
            ack_number=ack_number,
            data_offset=data_offset,
            CWR=CWR,
            ECE=ECE,
            URG=URG,
            ACK=ACK,
            PSH=PSH,
            RST=RST,
            SYN=SYN,
            FIN=FIN,
            window_size=window_size,
            checksum=checksum,
            urgent_pointer=urgent_pointer,
            options=options
        )


@dataclass
class PacketPayload:
    raw: bytes
    link_layer_header: int
    ip_header: IPHeader
    tcp_header: TCPHeader

    def __post_init__(self):
        assert self.link_layer_header == 2

    @classmethod
    def build(cls, data: bytes) -> "PacketPayload":
        link_layer_header = le2int(data[:4])
        ip_header = IPHeader.build(data[4:])
        tcp_header = TCPHeader.build(data[20:])
        return cls(
            raw=data,
            link_layer_header=link_layer_header,
            ip_header=ip_header,
            tcp_header=tcp_header,
        )



@dataclass
class Packet:
    header: PacketHeader
    payload: PacketPayload

    @property
    def raw(self) -> bytes:
        return self.header.raw + self.payload.raw

    @property
    def syn(self) -> int:
        return self.payload.tcp_header.SYN

    @property
    def ack(self) -> int:
        return self.payload.tcp_header.ACK

    @property
    def syn_ack(self) -> int:
        return int(self.syn and self.ack)

    @property
    def initiated(self) -> bool:
        return self.is_server_packet and self.syn

    @property
    def acked(self) -> bool:
        return self.is_client_packet and self.ack

    @property
    def is_client_packet(self) -> bool:
        return self.source_port == 80

    @property
    def is_server_packet(self) -> bool:
        return self.destination_port == 80

    @property
    def source_port(self) -> int:
        return self.payload.tcp_header.source_port

    @property
    def destination_port(self) -> int:
        return self.payload.tcp_header.destination_port


    @classmethod
    def create_packets(
        cls,
        data: bytes,
        header_length: int,
        n_packets: int | None = None,
    ) -> list[Optional["Packet"]]:
        packets = []
        counter = 0
        if n_packets is None:
            n_packets = len(data)
        while (
            tqdm(data) and
            counter < n_packets
        ):
            packet = cls.build(data, header_length)
            end_of_packet = header_length+packet.header.n_bytes_captured
            packets.append(packet)
            data = data[end_of_packet:]
            import pdb;pdb.set_trace()
            counter += 1
        return packets

    @classmethod
    def build(
        cls,
        data: bytes,
        header_length: int
    ) -> "Packet":
        packet_header = PacketHeader.build(
                data[:header_length]
            )
        end_of_packet = header_length+packet_header.n_bytes_captured
        payload = PacketPayload.build(data[header_length:end_of_packet])
        return Packet(header=packet_header, payload=payload)


def analyze_packets(packets: list[Packet]) -> None:
    print(len(packets))
    #print('CLIENT PACKETS')
    client_packets = [
        p for p in packets if p.is_client_packet
    ]
    print(len(client_packets))
    #clients = set(p.source_port for p in client_packets)
    #client_destinations = set(p.destination_port for p in client_packets)
    #clients_syn = [p for p in client_packets if p.syn]
    #clients_ack = [p for p in client_packets if p.ack]
    #clients_none = [p for p in client_packets if not p.ack and not p.syn]
    #assert len(clients) == 1
    #assert len(client_destinations) == 1
    #assert len(clients_syn) + len(clients_ack) + len(clients_none) == len(client_packets)

    ##print('SERVER PACKETS')

    #server_packets = [p for p in packets if p.is_server_packet]
    #server_syn_ack = [p for p in packets if p.syn_ack]
    #servers = set(p.destination_port for p in server_packets)
    #server_sources = set(p.source_port for p in server_packets)
    #assert len(servers) == 1
    #assert len(server_sources) == 1

    #print(
    #    f"Percentage of SYN Packets were SYN-ACKed: "
    #    f"{len(server_syn_ack)/len(clients_syn)*100:.2f}%"
    #)
    #print(
    #    f"Percentage of SYN Packets were ACKed: "
    #    f"{len(clients_ack)/len(clients_syn)*100:.2f}%"
    #)

    initiated_packets = [p for p in packets if p.initiated]
    acked_packets = [p for p in packets if p.acked]

    print('source ports')
    print(set((p.source_port for p in packets)))
    print('destination ports')
    print(set((p.destination_port for p in packets)))

    print(
        "Percentage of Acked Packets: "
        f"{len(acked_packets)/len(initiated_packets):.2f}%"
    )
    assert len(client_packets) + len(server_packets) == len(packets)
 

def main():
    with open(FILE, 'rb') as f:
        data = f.read()

    header = PCAPHeader.build(data)
    packets = Packet.create_packets(
        data=data[len(header.raw):],
        header_length=PACKET_HEADER_LENGTH,
        #n_packets=100
    )
    analyze_packets(packets)
   



if __name__ == '__main__':
    main()

