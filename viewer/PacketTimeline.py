from pcapfile import savefile

class PacketTimeline:

    def __init__(self, pcap_filename):
        with open(pcap_filename, mode='rb') as f:
            self.capfile = savefile.load_savefile(f)

        self.packets = self.capfile.packets #type = list
        self.start_time = self.packets[0].timestamp
        self.end_time = self.packets[-1].timestamp
        self.time_span = self.end_time - self.start_time

    def __iter__(self):
        return iter(self.packets)

    def packets_at(self, time):
        "takes in an epoch time and yeilds all packets with that same timestamp"
        for packet in self.packets:
            if packet.timestamp == time:
                yield packet
