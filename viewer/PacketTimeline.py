from pcapfile import savefile

class PacketTimeline(object):

    def __init__(self, pcap_filename):
        with open(pcap_filename) as f:
            self.capfile = savefile.load_savefile(f)

    def get_start_time(self):
        return self.timeline[0].timestamp

    def get_end_time(self):
        return self.timeline[-1].timestamp