import scapy.all as scapy

# create a function to call_back
def packet_callback(packet):

    # Check if the packet is IP
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        #Get protocol
        protocol = packet[scapy.IP].proto

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

        # Check if the packet is TCP
        if packet.haslayer(scapy.TCP):
            try:
                payload = packet[scapy.Raw].load
                decoded_payload = payload.decode('utf-8', 'ignore')
                print(f"TCP Payload")
            except (IndexError, UnicodeDecodeError):
                print("Unable to decode TCP payload.")

        elif packet.haslayer(scapy.UDP):
            try:
                # Check if raw layer exists
                payload = packet[scapy.Raw].load
                decoded_payload = payload.decode('utf-8', 'ignore')
                print(f"UDP Payload")
            except (IndexError, UnicodeDecodeError):
                print("Unable to decode UDP payload.")

def start_sniffing():
    scapy.sniff(store=False, prn=packet_callback)
# Start sniffing
start_sniffing()